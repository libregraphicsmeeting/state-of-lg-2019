# Welcome

* This is going to be a marathon. There are more projects than ever before, and more users, and more activity: Libre Graphics is alive and well! And the actions of big companies like Adobe, Autodesk and The Foundry also send many people our way. Let's welcome them!

# MrDocs

* Before we start I wish to say a few words in memory of Peter Linnel, mrdocs, who died in March. Being a professional in the print industry, he recognized the potential of Scribus, and worked really hard to realize that potential. With great success. His work in OpenSUSE was equally dedicated. And his presence at LGM is sorely missed. Let's remember Peter.

# Projects

## Layout

### Scribus

1. Scribus is a complete desktop publishing application.
2. The stable release improved support for Windows 10
3. The development branch sees code immprovements, the codebase is getting cleaned up and modernized, but more importantly, there are now nightly appimages, so everyone can play with it, especailly with the greatly improved Python Scripter API. 

Aside: Appimage really is a great technology.

### Laidout

1. Laidout is an application for experimenting with layouting, like the creation of physical flipbooks from animated gifs
2. You can now build content using nodes, using libraries like gegl and later on gmic
3. Check out Laidout at the Comic Book Workflow workshop on Saturday

## Raster

### Gimp

1. GIMP is a full-featured cross-platform image manipulation application.
2. Last year, GIMP 2.10 was released at LGM. Now GIMP also includes new features in stable releases, like new filters or line art detection in the bucket fill tool
3. The main development effort now is porting to GTK3, which is a huge refactoring.

### Krita

1. We released two full versions, 4.1 with the reference images tool and 4.2 with with support for HDR monitors on Windows. Since last month, there four people working full-time on Krita.
2. Krita is in fact the first painting application in the world to support HDR displays.
3. For the next release, 4.3, we're focusing on stability and bug fixing.

### MyPaint

1. MyPaint's current lead developer, Brien Dieterle, has been focusing on emulating paint media: putting the "paint" back into MyPaint. 
2. He is using an absorbance model which means mixing Blue and Yellow makes green! Overall "response" and "feel" is pretty satisfying but compatibility issues with premultiplied color have yet to be solved. And there are many performance issues.
3. Brien is also implementing canvas texture through bump mapping: the problem there is to have tiles without seams. There are lots of side-projects. As this is a one-man project at the moment, Brien needs help with project maintenance!

### Drawpile

1. Drawpile is a networked drawing application: people can work on the same drawing or animation with other people all over the world in real-time. Development was restarted in 2013.
2. Version 2.1 was released early 2019
3. The future will bring improved performance, layer groups and mypaint brush support.

### Photoflare

1. Photoflare is a cross-platform image editor built around GraphicsMagick. It started out as the C++ port of a delphi-based image editor called PhotoFiltre
2. In 2018, 2019, Photoflare has setup a smooth release system, with automatic appimage builds on travis, and has been accepted into Debian and Ubuntu.
3. Plans for the future include support for layers and mypaint brushes.

## Raster libraries

### Exiv2

1. Exiv2 is a cross-platform C++ library for handling Exif, IPTC and XMP metadata. Exiv2 is widely used.
2. The project has had a long history, has proven to be dependable, and the community is growing steadily.
3. Exiv2 0.27 was released December 2018. The next release will mostly be an internal refactoring, an update to C++11

### Gegl

1. GEGL and babl are libraries for manipulating high bit-depth pixel buffers.
2. Space Invasion is the name of the current project: support for colorspaces other than sRGB. This means CMYK support is coming.
3. And Gegl is getting its own UI again: to help developing the library. See you at Øyvind Kolås' talk here at 10:50.

### G'Mic

1. G'Mic is a framework for image processing. There are several user interfaces for working on images; the most popular ones are the Qt-based plugins for Gimp, Krita and Paint.net. The current version, 2.6, was released in April.
2. There are now more than 500 filters to play with! Two are especially spectacular. The first can illuminate a flat-colored drawing to give it a 3D look.
3. The second filter allows to transfer the style of one image onto a photograph: it tries to recreate the content of the photograph using elements from the style image. G'Mic now accepts donations, too.

## 3D

### Blender

1. Blender is the free and open source 3D creation suite. It supports the entirety of the 3D pipeline — modeling, rigging, animation, simulation, rendering, compositing and motion tracking
2. Blender 2.80 is the most anticipated blender release ever and is expected for July 2019. There's 3 years of work in it!
3. Workflow, the viewport but also the grease pencil have seen huge improvements.

### Dust3d

1. Dust3d is a quick 3D modeling application. It generates a mesh from nodes drawn by the user
2. In 2018, the 1.0 beta was released. 
3. And in 2019, the 1.0 final will be released.

## Vectors

### Inkscape (VIDEO !)

### sk1Project

1. sk1 2.0 is cross-platform vector-based illustration program. 
2. since 2017, the UniConverter application for converting between vector file formats has been integrated into sk1 and no longer exists standalone.
3. The next stable release will happen this summer

### Ommpfritt

1. Ommpfritt is a vector graphics editor where actions on shape objects are executed by objects, not by tools, so you get a non-destructive workflow.
2. It's more technical than inkscape. The concept was inspired by Cinema 4D and Blender, but it's entirely 2D. You can, for instance, add a clone object to your shape objects, and that will clone your shapes for you.
3. There's a talk about the concepts behind Ommpfritt on Friday! It's currently developed by one person, who would love collaborators.

### Birdfont

1. Birdfont is an open core truetype font editor: paid versions have more features, like support for OTF fonts.
2. Birdfont is considered "almost complete" by its developers, but a few new features have been added
3. TTF parsing has improved and support for Unicode 12 has been added

## Video and Movies


### KDenlive (VIDEO!)

1. KDenlive is a very full-featured cross-platform video editing application, using MLT. 
2. In April, version 19.04 was released. This represents 3 years of work, with a huge number of new features, improved features and performance improvements.
3. The team now strongly focuses on stability, but there are a number of new features planned as well, like OpenTimelineIO or text animations. And work has started on adding gpu accelerated rendering.

### Shotcut

1. Shotcut is also a full-featured, cross-platform video editor, using MLT.
2. Shotcut has a large team, but most activity comes from just the two main developers, who also develop the MLT library. The team needs to grow! The application itself is very popular.
3. 2018 was a busy year, with lots of new features, followed by lots of bug fixing. One of the new features was the addition of keyframes; another support for HTML for titles and effects, through QtWebKit.

### Morevna

1. Morevna Project is an animation studio that uses and develops open source software: Synfig OpenToonz, Papagayo, RenderChan 
2. This year, the Morevna team implemented Krita's assistant tool in OpenToonz. It's not merged in the official repo yet, but the Morevna team provides their own release.
3. The team works on their own open source anime series, called Morevna. This is based on the traditional Russian Fairy Tale Marya Morevna, but the animated series sets the events in a futuristisc sci-fi environment. You can watch the new episode, released today, at LGM as part of FILM MEETS FREE SOFTWARE on June 1st!

### Glosbevore (VIDEO)

1. A glosbevore is an eater of glass and it's an animated short film thats currently in post production and that has been created entirely with free software.
2. The animation is done by hand with a dslr camera. OpenToonz is used to create scenes from the images, blender for compositing, ardour for editing the soundtrack
3. teaser

## Raw

### Darktable

1. darktable is a high-precision raw converter and digital image manager. It's ten years old now, and the team has promised cake! 
2. The stable version has seen a lot of useful changes, like new image editing modules, export modules, UX improvements. The team wants to thank Pascal Obry for his enormous effort in development!
3. The development version will have a completely new user interface, huge speedups when putting 4k and 5k images on the lighttable, new darkroom modules. So many improvements, in fact, the team couldn't fit them on the admittedly crowded slides.

### Photoflow

1. Photoflow is a raw and raster image editor. It's five years old now, and actively developed.
2. The key features are advanced color management, including opencolorio, so editing and tonemapping of HDR images is supported. It's based on the VIPS processing pipeline, so large images can be worked on without running out of memory.
3. Recent developments include the OpenColorIO support and a lot of UI improvements.

### Filmulator

1. Filmulator is a RAW image developer application; it emulates developing physical film from RAW images. 
2. After LibRaw removed its demosaicing packs in the latest version, filmulator created a new library called librtprocess using the algorithms of RawTherapee. The library makes it possible to share new raw processing algorithms with other free software photo editors.
3. Next for Filmulator is improving library management and processing of very large images. And as for librtprocess, there's a meeting on Friday to discuss what direction the project should take.

## Education

### Flos Manuals Francophone

1. Floss Manuals Francophone collaboratively creates manuals for free and libre software in French. 

2. Books:

* Blender for video editing : 9 variously expert people experienced in Blender or video editing wrote in 5 days a book to learn how use Blender for video editing. They also created test videos.
* Cedric Gemy wrote a new book about Scribus for beginners
* Elisa de Castro Guerra wrote a book about Inkscape for beginners
* Floss Manuals Francophone help Sebastien Hache in writing a book about how write to educational manuals for school.

Floss Manuals Francophone also helped the English Floss Manuals by hosting a part of their infrastructure.

Floss Manuals Francophone also managed to sell about 100 real books about free graphic and free culture  to libraries and universities (arduino, processing, scribus, inkscape, fontes libres, etc). 


### Afgral

1. Association francophone des graphistes professionnels libre: the goal is to promote the use of free graphics software for professionnal use.
2. Afgral organizes workshops and events, like Grafik Labor. Afgral also organizes the "Open Video Game Award", where games developed with Blender and Godot can compete. There were four constestants, The winner was "Unhackneyed"  and that game can be downloaded from afgral.org!


### ActivDesign

1. ActivDesign is French art school. All courses only use free and libre graphics software. 
2. There are courses for graphic designer, game artist, game designer, illustrator, animator and so on. ActivDesign has been growing since 2011, and this year there are 25 students. There is also a studio space where everyone can work with with free free software!

### LILA

1. LILA is a French non-profit in France. The main project is the animation ZeMarmot, directet by Aryeom Han. To support Aryeom's work, development work on GIMP is done, too.
2. In 2018, the Framasoft non-profit commissioned a crowdfunding video for Peertube; LILA also designed enamel pins for the Free Software Foundation. Finally, LILA welcomed the popular G'Mic project under its umbrella. LILA is collecting donations to fund development.
3. ZeMarmot is still the main project, with Aryeom working on it full time, focusing on finishing the main pilot. Jehan is going to continue working on GIMP, having been a core team member for 7 years.

### pixels.us

1. PIXLS.US is a community of photographers focused on using and advancing Free Software. Its aim is to build a community based on _photography_ across many different (Free) projects.
2. The forum has just celebrated its 4th birthday, with traffic doubling every year. The RAW.PIXLS.US repository of freely licensed raw image files from as many cameras as possible has grown to 1239 files from 726 cameras. But that's not enough! Please help out. 
3. There are interesting new articles, interviews, tutorials and workflows, as well as a community sharing raw files so people can show each other there raw development workflow.

## Performance


### Upstage

1. UpStage is a web-based platform for cyberformance - live online digital performance. Artists located around the world collaborate in real time to create performances for online audiences, who only need a standard browser and internet to join the performance.
2. Last year, a complete rewrite of the platform started. The rebuild is called Limelight. Right now, performances still happen with Upstage v3, like the one on the slide: "Letters to the Earth" on 12 April 2019.
3. For the rewrite, the Upstage community would love to have help with programming, architecture, testing, documention -- everything! Everything is still in a very early stage, so there's room for everyone's input.

### Praxislive


1. PraxisLIVE is a hybrid visual live programming IDE and runtime, bringing aspects of Smalltalk, Erlang and Extempore into the Java world. It has a history and particular focus on creative coding and visualisation, with strong support for working with Processing, GStreamer video and custom OpenGL graphics.

2. PraxisLIVE v4 was released shortly after LGM 2018, with a wide range of improvements. The runtime was relicensed under LGPL so that it can be easily redistributed as part of a standalone project. Development through the year has focused on PraxisLIVE as a general 
purpose programming system, but still with benefits for creative
coding. 

3. In early 2019, generous sponsorship of the Java bindings for GStreamer, maintained as part of PraxisLIVE, allowed these to reach a first stable release. Improved access to GStreamer features is slowly being added to PraxisLIVE, with network streaming, video export and better GPU integration on its way.

~                                                  

# Envoi:

Libre Graphics is flourishing. I am exhausted. Let's have a great LGM!
