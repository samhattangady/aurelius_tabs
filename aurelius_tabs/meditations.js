var INDEX = 0;
var KEYS = Object.keys(MEDITATIONS);
var MAX_LENGTH = 300;

function getRandomIndex() {
  INDEX = Math.floor(Math.random() * Math.floor(KEYS.length));
  // TODO: Feels wrong to have this here. Should be in a nicer place.
  if (MAX_LENGTH > 0 && MEDITATIONS[KEYS[INDEX]].length > MAX_LENGTH) {
    return getRandomIndex();
  }
  return INDEX;
}

function setIndex(index) {
  let quote_id = KEYS[index];
  let text = MEDITATIONS[quote_id];
  document.getElementById('meditation').innerHTML = text;
  document.getElementById('source').innerHTML = quote_id;
}

function setRandom() {
  setIndex(getRandomIndex())
}

function setNext() {
  INDEX++;
  if (INDEX >= MEDITATIONS.length) { INDEX = 0; }
  setIndex(INDEX);
}

function setPrevious() {
  INDEX--;
  if (INDEX < 0) { INDEX = MEDITATIONS.length-1; }
  setIndex(INDEX);
}

function enableButtons() {
  document.getElementById('refresh').onclick = setRandom;
  document.getElementById('next').onclick = setNext;
  document.getElementById('previous').onclick = setPrevious;
}

enableButtons()
setRandom()

