function strings() {

  var s = 'abcdefghijklmnopqrstuvwxyz'
  console.log(s.length);
  console.log(s.charAt(12));
  console.log(s.substring(-1));    // anything < 0 will be treated as 0
  console.log(s.substring(2, 4));
  console.log(s.substring(13));
  console.log(s.substring(0, 8));
  console.log(s.substring(-1, 3)); // again, < 0 becomes 0.
  console.log(s.substring(0, -4)); // this basically does nothing.

}

