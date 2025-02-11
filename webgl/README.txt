
2023Jun13
This is a new directory for WebGL explorations, based primarily on the
book "WebGL Up and Running", by Tony Parisi
ISBN: 78-1-449-32357-8

The GitHub repo that goes with the book is here:
    https://github.com/tparisi/WebGLBook
    You can find images, code, etc.


        # running a local Python server
        $ python -m http.server 8000

2024Dec30

pgs10-15.html
    This is the introductory program which is basically making the point
    of how difficult it is to do webGL directly. Run the server above,
    it should render a page with white square on black background.
    2024Dec30: WORKING!

hello/
    This directory was apparently created by me in Feb 2024. Looks like
    source is coming directly from the ThreeJS site?

    At any rate, the important part is that it actually runs.
    Within the hello/ dir, run the python command above:

    Then load this URL in your browser:
        http://localhose:8000
    That should give you a browser listing of files in the directory,
    then just click on hello.html, and it should run!
    (It did on Monday, 2024Dec30)


pg20.html
    I copied the three.js from within hello/ into libs/Three.js to match
    the listing on pg 20. Typed in Page 20, ran it.
    OMG!! Working on first load!


# EOF
