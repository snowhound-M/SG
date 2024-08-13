import { React } from 'react';

function App() {
  const [myTodoList, setMyTodoList] = useState([]);
  const [myNewTask, setMyNewTask] = useState("");
  //const [myDeletedTask, setMyDeletedTask] = useState([]);
  const [myDeletedTaskList, setMyDeletedTaskList] = useState([]);

  function addTask() {
    setMyNewTask(event.target.value);
  }

  function addTaskToList() {
    const newTask = {
      id: myTodoList.length === 0 ? 1 : myTodoList[myTodoList.length - 1].id + 1,
      taskName: myNewTask
    };
    
    setMyTodoList([...myTodoList, newTask]);
  }

  function deleteTaskFromList(taskArg) {
    setMyTodoList(myTodoList.filter((myTask) => { return myTask.id !=== taskArg.id}));
    setMyDeletedTaskList([...myDeletedTaskList, taskArg]);
  }
  
  return (
    <>
      <div>
        <h1>TO-DO LIST</h1>
      </div>
      <div>
        <h3>ADD YOUR TASKS HERE</h3>
        <input type="text" onChange={addTask}></input>
        <button onClick={addTaskToList}>ADD</button>
      </div>
      <div>
        <h3>YOUR CURRENT TASKS</h3>
        {myTodoList.map((task) => {return <span>{task.id}.  {task.taskName} <button onClick={() => deleteTaskFromList(task)}>X</button></span>})}
      </div>
      <div>
        <h3> YOUR DELETED TASKS</h3>
        {myDeletedTaskList.map((task) => {return <span>{task.id}.  {task.taskName}  [ Deleted ]</span>})}
      </div>
    </>
  );
}
