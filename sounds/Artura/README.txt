ENGINE SOUNDS FOR: ARTURA

Put your engine loops in this folder, named by the engine speed (rpm) they were recorded at:

    1000.wav   2000.wav   3000.wav   ...   8000.wav

- Any rpm in steps of 500 (500, 1000, 1500 ... 10000). wav, mp3 or ogg.
- Use as many or as few as you like. Several files crossfade by rpm; ONE file is simply pitched up and down
  (name it for the rpm it was recorded at, e.g. 3000.wav).
- Each file should be a seamless loop at a steady rpm.
- No files here = the car uses a built-in sample.

HOW THE GAME FINDS THEM
- Served over http (for example run  python -m http.server  next to the html and open http://localhost:8000/Endless_Road_7.html):
  the game picks the files up by itself when you select this car.
- Opened by double-click (file://): the browser will not let a page read files by path.
  Open Settings (gear) > Audio > "Load sounds folder..." and pick the "sounds" folder once;
  the game keeps a copy in the browser, so you do not have to pick it again.
