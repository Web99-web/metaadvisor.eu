"""Read-only gate: it cannot authorize publication or activate redirects."""
import argparse
import json
import sys

def main():
    p=argparse.ArgumentParser();p.add_argument('--compat-report',required=True);p.add_argument('--validation',required=True)
    p.add_argument('--require-linux',action='store_true');a=p.parse_args()
    with open(a.compat_report,encoding='utf8') as f:c=json.load(f)
    with open(a.validation,encoding='utf8') as f:v=json.load(f)
    reasons=[]
    if c['pending']:reasons.append(f"{len(c['pending'])} unresolved route/feed decisions")
    if v['errors']:reasons.append(f"{len(v['errors'])} validation errors")
    if a.require_linux and (sys.platform!='linux' or not v.get('linux_build_confirmed')):reasons.append('Clean Linux build not confirmed')
    if reasons:raise SystemExit('RELEASE BLOCKED: '+ '; '.join(reasons))
    print('Technical gate passed. Publication still requires separate human approval.')

if __name__=='__main__':main()
