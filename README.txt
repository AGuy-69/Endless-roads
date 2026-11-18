ENDLESS ROAD
============

How to run
  Windows:       double-click serve.bat
  Mac / Linux:   run ./serve.sh   (or: sh serve.sh)
Both start a small local web server in this folder (needs Python 3) and open it in your browser.
The server turns caching off and picks a fresh port every time, so you always get the files in
this folder, never an old copy. Close the window / press Ctrl+C to stop.
Check the build number at the top right of the home screen. A fixed port:  serve.bat 9000   or   sh serve.sh 9000

Why not just double-click index.html?
  The sounds and car models are separate files in assets/. Browsers refuse to
  load files from other files when a page is opened straight from disk
  (file://), so the game shows a notice telling you to use serve.bat / serve.sh.

Folder layout
  index.html        the game (code only)
  assets/audio/     engine loops (engine_<car>_<rpm>rpm.wav) and tyre_squeal.wav
  assets/ui/        home screen + car selector (menu.css, carsel.css): logo_mark.svg, ico_*.svg, menu.css, tile_*.jpg (made by the game on first run)
  assets/models/    car_<name>.glb  (Ultimate Low-Poly Car Pack 1 + 2 by ProbablyNotG, CC BY 4.0)
  sounds/<car>/     OPTIONAL: your own engine loops, see sounds/README.txt
  checksums.txt     SHA-256 of every asset file

If a file is missing the loading screen names it and the game carries on
without it (for example, silent engine or the plain placeholder car).

Tile pictures
  The big home-screen tiles show photographs taken inside the game itself, in daylight: Race (two cars side by side),
  Free Drive, World, and Car, which shows whichever car you have selected (one picture per car).
  The Paint tile is different: it is a live picture of your selected car in your selected paint, retaken by the game
  every time you change the car or the colour (nothing is saved for it).
  The first time you start it, the game takes them behind the loading screen (about 15 seconds, once) and
  serve.bat / serve.sh saves them as assets/ui/tile_race / free / world / car_<id>.jpg. After that they just load.
  - Retake them any time: press F8 on the home screen.
  - Use your own pictures: replace those files (any JPG, roughly 960 px wide). Delete one and the game retakes it next start.
  - Started some other way than serve.bat / serve.sh? The pictures still appear for that session, but cannot be
    saved automatically; F8 then downloads them and you put them in assets/ui/ yourself.

Credits
  Car models: "Ultimate Low-Poly Car Pack" and "Ultimate Low-Poly Car Pack 2" by ProbablyNotG, CC BY 4.0.

Paint
  108 colours: 12 colour families (White, Silver, Black, Red, Orange, Yellow, Green, Teal, Blue, Purple, Pink, Brown),
  each in 9 shades from light to dark. In the garage open the Paint tab, pick the family, then the shade.
  Keys in the garage: Up/Down = family, Left/Right = shade, Tab = switch Cars/Paint. In the game: V = next family
  (Shift+V previous). Your colour is remembered between sessions.

Brake lights and the car's shadow (build 30)
  The red brake-light glow now only shines out of the back of the lamps and only lights surfaces behind the car
  (road, a car following you), fading smoothly to the sides: no glow beside or in front of the car.
  The dark patch around the car's footprint now follows the car's real top-down outline (made from its own model
  when it loads) instead of a rectangle.


Build 38: other cars' headlights no longer blow out to white. Their light now lifts the darkness off the road/car (keeps colour and texture), the beam haze is soft-capped, and your own bodywork gets less of it.

Build 39: water no longer glows at night (its own colour, foam and sun glint scale with daylight; noon unchanged).

Build 40: your own headlights use the same "lift the darkness" light as other cars, beam haze capped, new Settings > Headlight brightness slider (default 60%, saved).

Build 41: WORLD tile opens a World page: time of day and weather (instant), road winding (Gentle/Normal/Twisty), hills (Flat/Normal/Hilly), Apply & restart (same seed) and New random world. Winding/hills/seed go in the address (#seed123&wind1.6&hill1.5) and are remembered. No live picture updates.

Build 42: garage turntable halo is projected onto the road in the post pass (follows slopes and bumps, cannot cut through the ground) instead of flat discs.

Build 43: real weather. Rain (streaks that lean with your speed), snow, wet shiny roads with puddles, rain sound, storm lightning with delayed thunder. World page now says what applies instantly (time, weather) and the restart button only lights up when you changed road winding or hills.

Build 44: rain splashes (droplet crowns where drops hit ground/road/water, ripple rings on wet surfaces). Generated rain/thunder sound removed; hooks: WXF.rain (0..1) and WXF.onThunder(delaySeconds).

Build 45: rain no longer leans toward you at speed (stays upright with a faint slant).

Build 46: ripple rings removed; splash crowns and wet-road sheen kept.

Build 47: rain rings only on water (part of the water surface, never on cars). Waves scale with the size of the body of water: window.WAVE = { scale, cap, ref } (scale also a Settings slider "Wave size"). Sea = 1.0 (as before), a 400 m lake ~0.63, rivers the 0.12 floor.

Build 48: fixes "worker error: smoothstep is not defined" from build 47 (the chunk builder in the worker has no smoothstep; replaced with inline math). Tested by running the real worker code over a lake.

Build 49: rain box 32x22x32 -> 48x28x48 (15000 streaks, fades out 14-25 m), high-speed slant x1.7 (0.04 -> 0.068).

Build 50: automatic gearbox downshifts to keep the engine in the flat part of the torque curve (hard throttle: below 58% of the torque-peak rpm; light 45%; braking 52%; coasting 34%), never into a gear that would hit the limiter, no upshifting while braking, quicker second downshift. Manual: downshift refused if it would over-rev ("Too fast to downshift").

Build 55: seven new cars from "Ultimate Low-Poly Car Pack 2": M8, Urus, P1 GTR, GT-R, Mustang, AMG GT, Taycan (each converted to the game's car format: named paint/lights/glass, four separate wheels).
Build 56: the new cars drive like their real counterparts. Each has its own torque curve (CARSPEC "tc": rpm -> fraction of peak torque) built from the real figures: M8 Competition (4.4 V8 TT, 750 Nm 1800-5800 rpm),
  Urus Performante (4.0 V8 TT, 850 Nm 2300-4500), P1 GTR (V8 TT + electric motor filling the low end, 986 hp combined), GT-R Nismo (3.8 V6 TT, 652 Nm 3600-5600, ATTESA AWD, 6-speed DCT with the real ratios),
  Mustang GT (5.0 NA V8, torque peak 4900 rpm, power peak 7150, 10-speed auto), AMG GT R (4.0 V8 TT, 700 Nm 1900-5500, rear-mounted DCT), and masses/weight splits/top speeds from the makers' figures.
  These cars hold each gear close to their power peak at full throttle (CARSPEC "pwr") and are AWD-launched where the real car is.
  The Taycan Turbo S is electric: motor geared straight to the wheels (0 rpm at a standstill, full torque from the first turn, flat to ~5100 rpm, then constant power), up to 16,000 rpm,
  two-speed rear gearbox (very short 1st, taller 2nd; it changes up near 114 km/h), regenerative braking when you lift off, and a synthesized motor whine instead of engine loops (no sound files needed).
Build 57: Taycan sound reworked. Pitch follows motor rpm; loudness follows car speed: silent when parked, a low hum + body tone appear as it rolls and swell, then fade as speed builds while only a thin whine is left (louder on power, quieter on regen), with tyre/wind noise taking over at the top. Second detuned whine layer and a tiny slow pitch drift for realism; gearchange dips the volume.
Build 58: Taycan motor sound now fades linearly to nothing from 7,000 rpm (full volume up to 7,000, silent at its 16,000 rpm limit; EV_FADE0/EV_FADE1 in index.html). The wind/road rumble that used to be part of the Taycan sound is now a layer on every car (player, traffic and rivals): it reads the speed only, never throttle or rpm. N mutes it with the engine sound.
Build 59: Taycan motor sound is exactly 0% from 7,000 rpm up (linear fade down to it, EV_FADE0/EV_FADE1 in index.html). Wind (every car, speed only) is unchanged, so a fast Taycan is just wind and road noise.
Build 60: wind 1.5x quieter (peak gain 0.9 -> 0.6). Taycan motor sound now fades linearly to 0% at 10,000 rpm (EV_FADE1) and plays at the same level whether or not you are on the throttle (like a real EV); it only follows rpm.
