* [Up to "Table of contents"](../README.md)
* [Back to "8 Using self tapping screws"](../08-self-tapping-screws/Readme.md)
* [Next to "10 Referencing external parts"](../10-referencing-external-parts/Readme.md)

# 9 Creating a complex hinge

The next project regards a housing with a hinge. It can for instance be used for pencils or glasses. There is a magnet in each shell to lock the housing. An advantage of 3D printing is that we can pause printing at a designated layer to insert the magnets manually. When completed, the magnets are fully enveloped by the printed part.

This is the front view of the case when it is closed:

<p align="center">
  <img src="./images/front-view-closed.png" alt="Front view closed" width="641">
</p>

This is the front view of the case when it is open:

<p align="center">
  <img src="./images/front-view-open.png" alt="Front view open" width="694">
</p>

The details of the hinge are quite complex:

<p align="center">
  <img src="./images/rear-view-with-hinge.png" alt="Rear view with hinge" width="634">
</p>

The flat edges in the rear view are needed to avoid mechanical interference when the case is fully open, and they act as an end stop.

This is a cross section through the middle of the casing when it is closed:

<p align="center">
  <img src="./images/cross-section-closed.png" alt="Cross section closed" width="293">
</p>

This is a cross section through the middle of the casing when it is open:

<p align="center">
  <img src="./images/cross-section-open.png" alt="Cross section open" width="509">
</p>

The orientation of the parts during printing is the same as when the case is open. To bridge the openings of the magnets well, the top of the magnet opening needs to be horizontal during printing. This is why the magnet opening is not rectangular.

Four sketches define the general shape of the housing, for the top view and the right view, and for the internal and the external shape:

<p align="center">
  <img src="./images/sketches-housing.png" alt="Sketches housing" width="1150">
</p>

Two sketches define the hinge:

<p align="center">
  <img src="./images/sketches-hinge.png" alt="Sketches hinge" width="1049">
</p>

For the design of a 3D printed hinge it is important to take into account the accuracy of printing. There needs to be a slit of about 0.3 mm between the parts in all directions.

**sk hinge right** defines the right view of the hinge. The smallest (ø1.4 mm) circle represents the hole for the hinge pin. The circle around that represents the cylindrical shape of the hinge (which has a wall thickness of 1.35 mm). The outermost circle is a reference for the play (0.3 mm) between both parts of the housing.

<p align="center">
  <img src="./images/sketch-hinge-right.png" alt="Sketch hinge right" width="527">
</p>

The 135° angle is chosen to ensure both housing shells are printable without support structures.

The line going down is perpendicular to the bottom flat side of the housing. This line is a reference for the flat face mentioned above, ensuring the housing can be opened fully flat without mechanical interference.

There is also geometry representing the round parts of the hinge, **sk hinge top** basically divides the length of the hinge in three types of sections:
* elements that are connected to the bottom part of the housing
* elements that are connected to the top part of the housing
* space between the parts (S)

The sketch contains only two dimensions: the total length of the hinge and the space between the parts in axial direction. The radius of the cylinders is also modelled, but this has been derived from **sk hinge right**

<p align="center">
  <img src="./images/sketch-hinge-top.png" alt="Sketch hinge top" width="605">
</p>

The housing is modelled in two different bodies: **Housing external** represents the outside of the housing, **Housing internal** represents the cavity inside. The final housing is obtained by boolean subtraction in the part workbench.

## Housing external

The relevant sketches from the skeleton are imported as shape binders. The bottom and top datum plane are defined as 'normal to edge', referencing the Z-axis and the bottom  and top most points. The contour **he base** is modelled on **he pln bottom** and extruded until **he pln top**.

<p align="center">
  <img src="./images/housing-external-1.png" alt="Housing external 1" width="842">
</p>

**he chop off top** chops off the oblique surfaces of **HE Base**.

<p align="center">
  <img src="./images/housing-external-2.png" alt="Housing external 2" width="662">
</p>

A curve along the outside is made with a subtractive pipe using **he trim outside** along **he base**:

<p align="center">
  <img src="./images/housing-external-3.png" alt="Housing external 3" width="968">
</p>

Chamfers are added, **he ref hinge right** is imported and the flat edges for the end stop when opening the case are created:

<p align="center">
  <img src="./images/housing-external-4.png" alt="Housing external 4" width="857">
</p>

**he ref hinge top** is imported as shape binder, and the beginning- and end datum planes for the hinge are created. They exclude the space next to the hinge:

<p align="center">
  <img src="./images/housing-external-5.png" alt="Housing external 5" width="1088">
</p>

The cross section of the hinge **he hinge** is created on **he pln hinge left**, referring to **he ref hinge right** for the shape:

<p align="center">
  <img src="./images/housing-external-6.png" alt="Housing external 6" width="323">
</p>

**he hinge** is extruded from **he pln hinge left** to **he pln hinge right**, forming **HE Hinge**:

<p align="center">
  <img src="./images/housing-external-7.png" alt="Housing external 7" width="920">
</p>

As a final step for the hinge, the hole through the hinge is created:

<p align="center">
  <img src="./images/housing-external-8.png" alt="Housing external 8" width="952">
</p>

Both sketches determining the magnet pockets are imported, two planes defining the beginning and end of the magnet pockets are created, the lower magnet pocket is created, and the upper magnet pocket is mirrored from the bottom one:

<p align="center">
  <img src="./images/housing-external-9.png" alt="Housing external 9" width="878">
</p>

## Housing internal

The first steps of the Housing internal body are basically the same, but now referring to **sk housing internal top** and **sk housing internal right** instead of **sk housing external top** and **sk housing external right**:

<p align="center">
  <img src="./images/housing-internal-1.png" alt="Housing internal 1" width="762">
</p>

**hi ref magnet cavity top** is imported as shape binder. A rounded rectangle is sketched with a wall thickness around this shape in **hi room for magnets**. This is extruded from the shape in both directions as **HI Room for magnets**:

<p align="center">
  <img src="./images/housing-internal-2.png" alt="Housing internal 2" width="794">
</p>

Finally, a fillet is added to the magnet bump:

<p align="center">
  <img src="./images/housing-internal-3.png" alt="Housing internal 3" width="823">
</p>

## Housing

The housing is created by boolean subtraction of **Housing external** and **Housing internal** in the Part workbench:

<p align="center">
  <img src="./images/housing.png" alt="Housing" width="941">
</p>

## Separation bottom

The **Separation bottom** body starts with importing **sb ref housing external top** and **sb ref housing external right**, and then construction only **sb pln bottom**. A rectangle is drawn in a plane 0.1 mm below the XY plane, to ensure there is 0.2 mm space between both shells when the housing is closed, allowing for tolerances of 3D printing. The rectangle is 3 mm larger than the outer shape.

<p align="center">
  <img src="./images/separation-bottom-1.png" alt="Separation bottom 1" width="1175">
</p>

**sb ref hinge right** and **sb ref hinge top** are imported as shape binders. A positive revolve **SB Hinge positive volume** is added to the shape. The sketch **sb hinge positive volume** is a direct trace from **sb ref hinge top**.

<p align="center">
  <img src="./images/separation-bottom-2.png" alt="Separation bottom 2" width="929">
</p>

<p align="center">
  <img src="./images/separation-bottom-3.png" alt="Separation bottom 3" width="782">
</p>

Next we will create the slot for protrusion 2 from the top housing.

<p align="center">
  <img src="./images/separation-bottom-4.png" alt="Separation bottom 4" width="796">
</p>

Two datum planes are created, **sb pln hinge slot 2 begin** and **sb pln hinge slot 2 end**, which will be used for the second slot. They will include the space next to the slot.

<p align="center">
  <img src="./images/separation-bottom-5.png" alt="Separation bottom 5" width="639">
</p>

Line B of sketch **sb hinge slot** on datum plane **sb pln hinge slot 2 begin** is under an angle of 160° relative to line A of **sb ref hinge right**. This is because the top housing can be opened 160°, ensuring sufficient space between both parts. The larger circle in **sb ref hinge right** is used, to provide space radially.

<p align="center">
  <img src="./images/separation-bottom-6.png" alt="Separation bottom 6" width="933">
</p>

**SB Hinge slot 2** is extruded until **sb pln hinge slot 2 end**:

<p align="center">
  <img src="./images/separation-bottom-7.png" alt="Separation bottom 7" width="760">
</p>

**SB Hinge slot 4** is created by mirroring **SB Hinge slot 2** over the YZ plane.

<p align="center">
  <img src="./images/separation-bottom-8.png" alt="Separation bottom 8" width="991">
</p>

## Housing bottom

**Housing bottom** is a boolean intersection of **Housing** and **Separation bottom**

<p align="center">
  <img src="./images/housing-bottom.png" alt="Housing bottom" width="854">
</p>

## Separation top

**Separation top** is very similar to **Separation bottom**, only now the slots are in locations 1, 3 and 5. 

<p align="center">
  <img src="./images/separation-bottom-4.png" alt="Separation bottom 4" width="740">
</p>

Slots 1 and 3 were created individually, slot 5 is a mirror of slot 1.

<p align="center">
  <img src="./images/separation-top.png" alt="Separation top" width="1079">
</p>

## Housing top

**Housing top** is a boolean intersection of **Housing** and **Separation top**

<p align="center">
  <img src="./images/housing-top.png" alt="Housing top" width="734">
</p>


## Final checks

The **Dependency graph** and **Check geometry tool** that as described earlier reported no errors.

The **Persistent section cut** also reveals no problems:

<p align="center">
  <img src="./images/hinge-check.png" alt="Hinge check" width="509">
</p>

The **Printability inspection** also looks good:

<p align="center">
  <img src="./images/printability-test-1.png" alt="Printability test 1" width="783">
</p>

* [Up to "Table of contents"](../README.md)
* [Back to "8 Using self tapping screws"](../08-self-tapping-screws/Readme.md)
* [Next to "10 Referencing external parts"](../10-referencing-external-parts/Readme.md)

