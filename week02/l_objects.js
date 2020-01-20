function objects() {
  function Pet(name, age) {
    this.name = name;
    this.age = age;

    this.toString = function() {
      return this.name + ' is ' + this.age;
    };
  }


  let pets = [
    new Pet('Fido', 4),
    new Pet('Spot', 7),
    new Pet('Bubbles', 1)
  ];

  console.log(pets[0].toString());
  console.log(pets[1] instanceof Object);
  console.log(pets[2] instanceof Pet);
}

