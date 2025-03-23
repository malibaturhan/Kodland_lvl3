from db_man import *

def add_task_db(gives_charge_id:int, takes_charge_id:int, task_def:str):
    result =  execute_query(
        "INSERT INTO task (user_gave_id, user_took_id, task_def) VALUES (?,?,?)",
        (gives_charge_id, takes_charge_id, task_def)
    )
    return result
        
def delete_task_db(task_id:int):
    return execute_query("DELETE FROM task WHERE id=?", (task_id,))

def complete_task_db(task_id:int):
    return execute_query("UPDATE task SET completed = 1 WHERE id =?", 
                                  (task_id,)
                                  )

def get_all_tasks_db():
    tasks = execute_query(
        "SELECT id, user_gave_id, user_took_id, task_def, completed FROM task"
    )
    if len(tasks) == 0:
        return "no tasks at all"
    return "\n".join([f"{task[0]} | {task[3]} | {'✅' if task[4] == 1 else '❌'}" for task in tasks])

def add_user_db(uid: int ,username: str):
    result = execute_query(
        "INSERT INTO user (uid, user_name) VALUES (?, ?)",
        (uid ,username)
    )
    return result