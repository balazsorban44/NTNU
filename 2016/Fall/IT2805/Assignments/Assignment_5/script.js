/* Part 2 */
console.log('PART 2')

for (i=1; i<21; i++){
  console.log(i)
}

/* Part 3 */
console.log('PART 3')

const numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
for (i=0; i<numbers.length;i++){
  if (numbers[i]%3==0 && numbers[i]%5==0) {
    console.log("eplekake");
  }
  else if (numbers[i]%3==0) {
    console.log("eple");
  }
  else if (numbers[i]%5==0) {
    console.log("kake");
  }
  else {
    console.log(numbers[i]);
  }
}
/* Part 4 */
  document.getElementById('title').innerHTML="Hello, JavaScript";
/* Part 5 */
var e = document.getElementById('magic')
function changeDisplay(){
  e.style.display="none"
}

function changeVisibility(){
  e.style.display="block"
  e.style.visibility="hidden"
}

function reset(){
  e.style.display="block"
  e.style.visibility="visible"
}

/* Part 6 */
const technologies = [
  'HTML5',
  'CSS3',
  'JavaScript',
  'Python',
  'Java',
  'AJAX',
  'JSON',
  'React',
  'Angular',
  'Bootstrap',
  'Node.js'
];
for (i=0; i<technologies.length;i++){
  document.getElementById("tech").innerHTML+= "<li>" + technologies[i] + "</li>"
  /*Simply inserting the array values into the ul tag as in Part4. Notice the '+=' which appends the next value at the end,
  so it won't just overwrite the previous li tag.*/
}
