let img = document.querySelector('#shape-back');
let btnCngLearnNext = document.querySelector('#learn-shape-next-btn');
let btnCngLearnBack = document.querySelector('#learn-shape-back-btn');
var shapeImageLearnCount = 0;

img.src = "/media/knowYourself/imageDB/"+shapeImageLearnCount+".jpg"

btnCngLearnNext.addEventListener('click' , ()=>{
  shapeImageLearnCount++;
  img.src = '/media/knowYourself/imageDB/'+shapeImageLearnCount+'.jpg';
})

btnCngLearnBack.addEventListener('click' , ()=>{
  shapeImageLearnCount--;
  img.src = '/media/knowYourself/imageDB/'+shapeImageLearnCount+'.jpg';
})

function path(){
  return '/media/knowYourself/imageDB/'+shapeImageLearnCount+'.jpg'
}