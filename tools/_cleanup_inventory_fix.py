from pathlib import Path
p=Path(__file__).with_name('_cleanup_course_repo.py')
s=p.read_text()
a="    old=load_json(root/'PROMOTION-RECORD.json')\n"
b="    if digest(json.dumps(retired,sort_keys=True,separators=(',',':')).encode())!='__INVENTORY_HASH__': raise ValueError('Historical recovery inventory changed')\n"+a
assert s.count(a)==1
s=s.replace(a,b,1)
a="code=exact(code,'def check(root: Path) -> None:\\n',helpers+'def check(root: Path) -> None:\\n')"
b="helpers=helpers.replace('__INVENTORY_HASH__',digest(json.dumps(retired,sort_keys=True,separators=(',',':')).encode()))\n"+a
assert s.count(a)==1
p.write_text(s.replace(a,b,1))
Path(__file__).unlink()
