from pathlib import Path
import json,sys
root=Path(__file__).resolve().parents[1]
a=json.loads((root/'migration/release-approvals.json').read_text(encoding='utf-8'))
keys=('publication_approved','linux_qa_completed','http_migration_layer_approved','regional_analytics_review_completed')
blocked=[k for k in keys if a.get(k) is not True]
if blocked:
 print('RELEASE BLOCKED: '+', '.join(blocked));sys.exit(2)
print('Explicit release approvals present; this check performs no publication.')
