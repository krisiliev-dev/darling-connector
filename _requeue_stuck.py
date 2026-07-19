import run_one, json
STUCK = ["200102","190246","200609","0114148","1535","018831"]
for c in STUCK:
    task, fc = run_one.next_task(c)
    if not task:
        print(c, "-> no task"); continue
    print(c, "->", run_one.process_agentic(task, 0), flush=True)
print("done")
