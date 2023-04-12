module LuciansLusciousLasagna

// define the 'expectedMinutesInOven' binding
let expectedMinutesInOven = 40

// define the 'remainingMinutesInOven' function
let remainingMinutesInOven bakedMin =
    expectedMinutesInOven - bakedMin

// define the 'preparationTimeInMinutes' function
let preparationTimeInMinutes nLayers =
    nLayers * 2

// define the 'elapsedTimeInMinutes' function
let elapsedTimeInMinutes nLayers bakedMin =
    preparationTimeInMinutes(nLayers) + bakedMin
