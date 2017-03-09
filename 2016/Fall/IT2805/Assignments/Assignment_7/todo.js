undoneTasks = [];
doneTasks = [];
var inputArea = document.getElementsByTagName('input')[0];
var tasks = document.getElementById("tasks");

/*------------------------------------This function renders the done and undone undoneTasks.----------------------------------*/
function refresh(array1, array2) {

  /*-----Sorting the undone undoneTasks.---*/
  array1.sort(function(a, b) {
    return parseFloat(parseFloat(b.timestamp) - a.timestamp);
  });

  /*-----Emptying the unordered tasks to avoid duplicates in the next step.---*/
  while (tasks.firstChild) {
    tasks.removeChild(tasks.firstChild);
  }

  /*------This loop puts the newly added undoneTasks to the unordered tasks.------------*/
  for (i = 0; i < array1.length; i += 1) {
    var task = document.createElement("li");
    task.setAttribute("onclick", "checkCheckBox()")
    task.setAttribute("title", "Click to check this task.");

    var checkBox = document.createElement("input");
    var removeTask = document.createElement("span");
    removeTask.setAttribute("title", "Remove this task from the list.");
    removeTask.setAttribute("onclick", "removeTask()")
    checkBox.setAttribute("type", "checkbox");
    task.appendChild(checkBox);
    task.appendChild(document.createTextNode(array1[i].task));
    task.appendChild(removeTask);
    task.id = array1[i].timestamp;
    tasks.appendChild(task);
  }
  /*-----This loop puts the checked undoneTasks at the bottom of the unordered tasks.---*/
  for (i = 0; i < array2.length; i += 1) {
    var task = document.createElement("li");
    task.setAttribute("onclick", "unCheckCheckBox()");
    task.setAttribute("title", "Click to uncheck this task.");
    var checkBox = document.createElement("input");
    checkBox.setAttribute("type", "checkBox");
    checkBox.checked = true;
    task.appendChild(checkBox);
    task.appendChild(document.createTextNode(array2[i].task));
    task.id = array2[i].timestamp;
    task.style.textDecoration = "line-through";
    tasks.appendChild(task);
  }

  /*-----------------------Writing out the done/all undoneTasks.------------------------*/
  document.getElementById("out").value = doneTasks.length + "/" + (undoneTasks.length + doneTasks.length) + ":"

  /*-----Revert to the main input field.---*/
  inputArea.value = "";

}

/*-----------------------Add a new task to the the undone array as an object. ------------------------*/
function addTask(array) {

  /*-----If statement to avoid empty undoneTasks.---*/
  if (inputArea.value != "") {
    undoneTasks.unshift({
      timestamp: new Date().getTime(),
      task: inputArea.value
    });

    /*-----Run tasks rendering.---*/
    refresh(array, doneTasks);
    inputArea.placeholder = "Click + or press Enter.";
  }

  /*-----Asks the user to do not make empty undoneTasks.---*/
  else {
    inputArea.placeholder = "Write something...";
  }
}

function removeLastTask(array) {
  array = array.splice(0, 1)
  refresh(undoneTasks, doneTasks);
}

function removeTask() {
  var task = event.target.parentNode
  for (i = 0; i < undoneTasks.length; i += 1) {
    if (task.id == undoneTasks[i].timestamp) {
      undoneTasks.splice(i, 1)
    }
  }

  /*-----Run tasks rendering.---*/
  refresh(undoneTasks, doneTasks)
}

/*-----------------------Move checked element into the done array.------------------------*/
function checkCheckBox() {
  if (event.target.tagName == "INPUT") {
    var task = event.target.parentNode
  } else if (event.target.tagName == "LI") {
    var task = event.target
  } else {
    return
  }
  doneTasks.unshift({
    timestamp: parseInt(task.id),
    task: task.innerText
  });
  for (i = 0; i < undoneTasks.length; i += 1) {
    if (task.id == undoneTasks[i].timestamp) {
      undoneTasks.splice(i, 1)
    }
  }

  /*-----Run tasks rendering.---*/
  refresh(undoneTasks, doneTasks)
}

/*-----------------------Move unchecked element back to the undone array.------------------------*/
function unCheckCheckBox() {
  if (event.target.tagName === "INPUT") {
    var task = event.target.parentNode
  } else {
    var task = event.target
  }
  undoneTasks.unshift({
    timestamp: parseInt(task.id),
    task: task.innerText
  });
  for (i = 0; i < doneTasks.length; i += 1) {
    if (task.id == doneTasks[i].timestamp) {
      doneTasks.splice(i, 1)
    }
  }

  /*-----Run tasks rendering.---*/
  refresh(undoneTasks, doneTasks)
}
