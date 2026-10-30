#!/usr/bin/env bash
# No installation, Git mutation, upload or deployment. Run against a disposable complete source copy.
set -euo pipefail
repo=$(realpath "${1:?source directory}")
out=$(realpath -m "${2:?new output directory outside source}")
[[ $(uname -s) = Linux ]]
[[ ! -e "$out" ]]
case "$out/" in "$repo/"*) echo "Output must be outside source" >&2; exit 2;; esac
hugo version | grep -F 'v0.128.0' | grep -F extended
python3 -c 'import lxml'
mkdir -p "$out"
cd "$repo"
GIT_OPTIONAL_LOCKS=0 GIT_NO_LAZY_FETCH=1 git ls-files --stage -z > "$out/index-before.bin"
python3 tools/prepare_tag_archives.py --check
python3 -c 'import json,sys; print("resourceDir = "+json.dumps(sys.argv[1]))' "$out/resources" > "$out/resource-overlay.toml"
GOMAXPROCS=4 HUGO_ENVIRONMENT=production hugo --minify --config "$repo/config.toml,$out/resource-overlay.toml" --destination "$out/public" --cacheDir "$out/cache" --ignoreCache > "$out/hugo.log" 2>&1
printf '{"platform":"linux","returncode":0,"publication":false}\n' > "$out/linux-build.json"
python3 tools/repair_verified_urls.py --output "$out/public" --report "$out/repairs.json"
python3 tools/build_tag_compatibility.py --output "$out/public" --report "$out/compatibility.json"
python3 tools/finalize_release.py --output "$out/public" --report "$out/final-policy.json"
python3 tools/validate_tag_release.py --output "$out/public" --compat-report "$out/compatibility.json" --report "$out/validation.json" --require-linux
GIT_OPTIONAL_LOCKS=0 GIT_NO_LAZY_FETCH=1 git ls-files --stage -z > "$out/index-after.bin"
cmp "$out/index-before.bin" "$out/index-after.bin"
echo 'Linux QA finished. This is not publication approval and does not activate migrations.'
