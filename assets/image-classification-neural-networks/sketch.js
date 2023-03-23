let classifier;
let testImage;
let sampleImage;

function preload(){
  classifier = ml5.imageClassifier("model.json", teachableMachineModelLoaded);
  testImage=loadImage("testing0.jpg");
  console.log("Successfully Loaded Test Image");
}

function setup(){
  // Output the current version of ml5 to the console
  console.log('ml5 version:', ml5.version);
  // Create a blank square canvas that is 500px by 500px 
  createCanvas(500,500);
  background('#000000');
}

function draw(){
  // Set the background of the canvas to black based on the hex code 
  imageMode(CENTER);
  image(testImage, width/2, height/2);
  noLoop();
  classifier.classify(testImage, gotResults); 
}

function gotResults(error, results) {
  if (error) {
    console.error(error);
  } else {
    fill(255, 255, 255);
    textSize(30);
    textAlign(CENTER)
    text("Most Likely " + results[0].label, width/2 , height/2+200);
    console.log("Most likely " + results[0].label);
    console.log(results);
  }
}

function teachableMachineModelLoaded(){
  console.log("Teachable Machine Model Successfully Loaded");
}