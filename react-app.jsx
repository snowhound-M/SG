import { React } from 'react';

function App() {
  const [myTodoList, setMyTodoList] = useState([]);
  const [myNewTask, setMyNewTask] = useState("");

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

  function deleteTaskFromList() {
    setMyNewTask(event.target.value);
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
        {myTodoList.map((task) => ({task.id}. {task.taskName} <button>X</button>))}
      </div>
      <div>
              <h3>YOUR CURRENT TASKS</h3>
  {myTodoList.map((task) => return <span>{task.id} {task.taskName}</span> <button> X </button>}
</div>
      <div>
        <h3> YOUR DELETED TASKS</h3>
        {}
      </div>
    </>
  );
}
