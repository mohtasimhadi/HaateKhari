let img = document.querySelector('#shape-back');
let btnCngLearnNext = document.querySelector('#learn-shape-next-btn');
let btnCngLearnBack = document.querySelector('#learn-shape-back-btn');
var shapeImageLearnCount =0;

btnCngLearnBack.style.visibility = 'hidden';

btnCngLearnNext.addEventListener('click' , ()=>{
    if ( shapeImageLearnCount == 0) {
        img.src = '/media/temp/Face.jpg';
        shapeImageLearnCount++;
        btnCngLearnBack.style.visibility = 'visible';
    }
    else if(shapeImageLearnCount == 1){
        img.src = '/media/temp/Nose.jpg';
        shapeImageLearnCount++;

    }
    else if(shapeImageLearnCount == 2){
        img.src = '/media/temp/Eye.jpg';
        shapeImageLearnCount++;
    }
    else if(shapeImageLearnCount == 3){
        img.src = '/media/temp/Mouth.jpg';

        btnCngLearnNext.style.visibility = 'hidden';
    }

})

btnCngLearnBack.addEventListener('click' , ()=>{
    if ( shapeImageLearnCount == 3) {
        img.src = '/media/temp/Mouth.jpg';
        shapeImageLearnCount--;

    }
    else if(shapeImageLearnCount == 2){
        img.src = '/media/temp/Eye.jpg';
        shapeImageLearnCount--;

    }
    else if(shapeImageLearnCount == 1){
        img.src = '/media/temp/Nose.jpg';
        shapeImageLearnCount--;
    }
    else if(shapeImageLearnCount == 0){
        img.src = '/media/temp/Face.jpg';
        btnCngLearnBack.style.visibility = 'hidden';
        btnCngLearnNext.style.visibility = 'visible';
    }
})