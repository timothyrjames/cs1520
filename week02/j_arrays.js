function arrays() {
  let names = ["Kanye", "Eminem", "Jay-Z"];
  console.log(names);

  let myList = new Array();
  myList.push(5);             // use "push" instead of "append"
  myList.push(3.2);
  myList.push(true);
  myList.push('something');

  console.log(myList);

  let numList = [];           // just like in Python, this is common

  for (var i = 0; i < 10; i++) {
    numList.push(i * 100);
  }

  console.log(numList);
  console.log(numList.slice(3, 5));
  console.log(numList.slice(3));
}
