# Introduction
This tutorial demonstrates how to design 3D printable housings in FreeCAD. The advantage of this approach is that it is quite structured, and you can manage changes in the design quite well, even if the design gets complex.

To follow this tutorial, you need to be familiar with the part design workbench and the sketcher. I’ll try to just focus on a high conceptual level.

# Topics in this document
- [Introduction](#introduction)
- [Topics in this document](#topics-in-this-document)
- [Concept of making a housing using boolean operation of bodies](#concept-of-making-a-housing-using-boolean-operation-of-bodies)
- [Making changes to the housing](#making-changes-to-the-housing)
- [Maintaining the colors of both housing bodies](#maintaining-the-colors-of-both-housing-bodies)
- [Applying a naming convention for bodies and features](#applying-a-naming-convention-for-bodies-and-features)
- [Using a skeleton to drive dimensions of the bodies](#using-a-skeleton-to-drive-dimensions-of-the-bodies)
- [Checking the model](#checking-the-model)
  - [Checking links](#checking-links)
  - [Using the Check geometry tool](#using-the-check-geometry-tool)
  - [Checking the result in the slicer](#checking-the-result-in-the-slicer)
- [Creating references to the internal components of the housing](#creating-references-to-the-internal-components-of-the-housing)
- [Using self tapping screws to close the housing](#using-self-tapping-screws-to-close-the-housing)
  - [Creating a screw hole](#creating-a-screw-hole)
  - [Creating a pillar for the screw](#creating-a-pillar-for-the-screw)
- [Creating a complex hinge](#creating-a-complex-hinge)
- [Creating references to external parts](#creating-references-to-external-parts)

# Concept of making a housing using boolean operation of bodies
I this example, we want to create a housing which consists of two shells which can be assembled together:
1. Create the housing (1) as a single body, without worrying about the separation.
2. Create a second body (2) separation top, which covers which part of the housing will become the top half of the housing
3. Create a bottom separation (3) as a third body in the same way
4. Create the top housing as a boolean operation between the housing and the top separation
5. Create the bottom housing as a boolean operation between the housing and the bottom separation

![Concept](./images/01-concept/concept.png)

Create the first body named **Housing** (1). In this example it consists of an additive loft for the outside and a subtractive loft for the internal cavity.

<p align="center">
  <img src="./images/01-concept/housing.png" alt="Housing body" width="650">
</p>

Then create another body in the same part, and call it **Separation top** (2). In this example, it consists of a pad and an additive pipe to create the rim. Note that the pad is deliberately larger than the housing: since we will create a boolean operation lateron, the exact size does not matter.

<p align="center">
  <img src="./images/01-concept/separation-top.png" alt="Separation top" width="650">
</p>

Also create **Separation bottom** (3) as a separate body.

<p align="center">
  <img src="./images/01-concept/separation-bottom.png" alt="Separation bottom" width="650">
</p>

Next move to the part workbench. Select **Housing** and **Separation top**, and choose the `Intersection` command from the toolbar.

<p align="center">
  <img src="./images/01-concept/housing-top.png" alt="Housing top" width="650">
</p>

Thus a new body named **Common** is created, consisting of the boolean intersection of both selected bodies. Rename that body **Housing top** (1 & 2).

It may seem as if the **Housing** body has disappeared from the model tree, so we can no longer select it to create the bottom housing. However, if we expand the **Housing top** body, we can see that **Housing** is still there since it was used to make up the **Housing top**. Select the **Housing** body and the **Separation bottom** body and apply the `Intersection` command again on those two bodies. The resulting body is named **Common 001**. Rename it to **Housing bottom** (1 & 3).

<p align="center">
  <img src="./images/01-concept/housing-bottom.png" alt="Housing top" width="650">
</p>

After modifying the color and transparency of both housing parts, the result looks like this:

<p align="center">
  <img src="./images/01-concept/result.png" alt="Result" width="650">
</p>


# Making changes to the housing

One could argue that the drawback of this method is that we can no longer modify both **Housing top** and **Housing bottom** using the part design workbench. In practice this is not a problem, since we can make those modifications to the three bodies we started with. However, it is important to make a considerate decision about on which body to make the modification. For instance, if the housing is used to support some electronics, and we need a power cable to connect to the electronics inside, we can simply add those features to the original **Housing** body.

Ensure that **Housing** is the only visible body, and that it is the active part by doubleclicking it.

<p align="center">
  <img src="./images/02-making-modifications/selecting-housing.png" alt="Selecting housing" width="650">
</p>

Next, add a protrusion and a hole to the housing for the power connector.

<p align="center">
  <img src="./images/02-making-modifications/modifying-housing.png" alt="Modifying housing" width="650">
</p>

After making the **Housing** body invisible and the **Housing bottom** and **Housing top** bodies visible, we can see that both bodies were modified:

<p align="center">
  <img src="./images/02-making-modifications/result.png" alt="Result" width="650">
</p>

Please note that this operation has overwritten the colors of the **Housing bottom** and **Housing top** bodies. We can again correct these colors, but this soon becomes annoying and so we apply a simple workaround to avoid that.


# Maintaining the colors of both housing bodies

The simplest workaround is to create a copy of the bodies and apply the desired color to this copy.

Switch to the **Part workbench** and select the **Housing top** body.

<p align="center">
  <img src="./images/03-maintaining-colors/refine-shape.png" alt="Result" width="650">
</p>

Rename the copied body **Housing top refined** and modify color and transparency. Repeat this for **Housing bottom**.

<p align="center">
  <img src="./images/03-maintaining-colors/result.png" alt="Result" width="650">
</p>

The colors of the refined shapes will remain unchanged if the original bodies are modified.

Another advantage of this workaround is that we can create multiple copies in various positions. This way we can easily inspect the parts in different orientations by making the right combination visible.

<p align="center">
  <img src="./images/03-maintaining-colors/different-orientations.png" alt="Result" width="650">
</p>

# Applying a naming convention for bodies and features

If the number of bodies and features in the model tree grows, it becomes increasingly difficult to indentify the right feature if you want to make changes. It becomes helpful to choose unique and meaningful names for features. I have developed my own system which is as follows:

| Type of feature         | Case          | Code              |
|-------------------------|---------------|-------------------|
| Volumetric features     | Sentence case | `Bd Name`         |
| Non-volumetric features | lowercase     | `bd typ name ext` | 

Non-volumetric features such as sketches and planes use lower case names. Volumes use Sentence case names (e.g., a sketch may be named **hs base**, and the pad that is created using that sketch is named **HS Base**)

| Code   | Meaning                                                                                                              |
|:------:|----------------------------------------------------------------------------------------------------------------------|
| `Bd`   | a loose abbreviation of the body (**HS** for housing, **ST** for separation top, **SB** for separation bottom, etc.) |
| `Typ`  | a 3 letter code for the type of feature after that abreviation: <br> **pln** for a plane <br> **axs** for an axis <br> **ref** for a shape binder |
| `Name` | The name of the feature |
| `ext`  | for additive and subtractive pipes: <br> the trajectory of the pipe is followed by **trj** <br> the cross section is followed by **crs** |

Examples:

| Name of the feature | Purpose                                                                                             |
|---------------------|-----------------------------------------------------------------------------------------------------|
| `sk top`            | Top view of the part in the **Skeleton** body                                                       |
| `hs ref top`        | Shape binder in the housing body, referencing the top view in the **Skeleton** body                 |
| `hs pln bottom`     | Datum plane in the housing body, representing the bottom of the **Housing** body                    |
| `sb groove crs`     | Cross section of the groove in the **Separation bottom** body                                       |
| `sb groove trj`     | Trajectory of the groove in the **Separation bottom** body                                          |
| `SB Groove`         | The 3D groove in the **Separation bottom** body, made up of **sb groove crs** and **sb groove trj** |

It is helpful to choose a pragmatic approach: for simple projects, the overhead of renaming every feature may not be worth the effort.


# Using a skeleton to drive dimensions of the bodies

As can be seen in this example, it would be helpful to create links between the different bodies to make the design truly parametric. For instance, the rim is defined in the **Separation top** and **Separation bottom** bodies, but they need to follow the contour that is defined in the **Housing** body. One body can reference another body, but the reference can only be in one direction: once features of a body B are referencing body A, there can no longer be a reference from body A to body B.

One way of keeping this structured is to start with a **Skeleton** body which only holds some basic shapes and dimensions, but that does not represent any volumes. This **Skeleton** body is then referenced by the other bodies.

Another advantage of a skeleton body is that it makes the model more robust. If sketches refer to 3D geometry, such as edges of the body, the model quickly becomes unstable since names of those edges are changed when making small changes (the notorious [Topological Naming Problem](https://wiki.freecad.org/Topological_naming_problem) ). When referring to edges in sketches instead, it is less likely that names of those edges are changed. This is especially true if we keep these sketches small and simple. It is therefore better to create a large number of simple sketches instead of a few complex ones.

In this example, the **Skeleton** body contains a number of sketches:
* **sk front**: the front view of the housing 
* **sk separation**: the separation lines for both the top and the bottom separations
* **sk bottom**: the bottom view of the housing
* **sk rim trj**: the trajectory that the rim and the groove must follow
* **sk rim crs**: the cross sections of both the rim and the groove

Besides, it also contains some helper planes that were used to create these sketches. The sketches also refer to each other: for instance, the length of the housing is both defined in **sk front** and in **sk bottom**. Therefore, **sk bottom** refers to **sk front** to obtain the length so the length is defined only once.

<p align="center">
  <img src="./images/05-skeleton-body/skeleton.png" alt="Result" width="650">
</p>

Now create a second body with the name **Housing**. It is not possible to create links to sketches in other bodies like we are used to. We first need to create a *Shape binder*:
* Ensure that **Housing** is the active body
* Select the **sk front** sketch in the **Skeleton** body
* Use the `Create a sub-object(s) shape binder`-button on the toolbar to create a shape binder
* Rename the shape binder **hs ref front** (I will explain the name convention later)

<p align="center">
  <img src="./images/05-skeleton-body/shape-binder.png" alt="Result" width="650">
</p>

Repeat the procedure for **sk bottom** and rename is **hs ref bottom**. Now make the **Skeleton** body invisible using the spacebar. Then create a plane where the bottom sketch will be drawn:
1. Select the Z-axis of the **Housing** body in the model tree, 
2. Also select a point at the bottom of the housing in the model.

<p align="center">
  <img src="./images/05-skeleton-body/select-z-axis-and-point-on-bottom.png" alt="Result" width="500">
</p>

3. Now create a plane using the `Datum Plane` button on the toolbar
4. Select 'normal to edge' in the Datum plane parameter window and click OK

<p align="center">
  <img src="./images/05-skeleton-body/create-bottom-plane.png" alt="Result" width="500">
</p>

We now have a plane that we can use for the bottom sketch. Now create the bottom sketch of the housing by simply tracing the **hs ref bottom** shape binder.

Repeat the same procedure with the top plane. It is possible to reference the oblique edge of the front view by changing the sketch view to isometric and selecting the oblique edge

<p align="center">
  <img src="./images/05-skeleton-body/selecting-nose.png" alt="Result" width="600">
</p>

A chamfer is added to the top and bottom edges of the housing. The cavity inside the housing is created in a similar way as the outer shape.

<p align="center">
  <img src="./images/05-skeleton-body/housing.png" alt="Result" width="600">
</p>

Note that:
* the main outer dimensions of the housing can be changed by only changing dimensions in the **Skeleton** body
* not all sketches from the **Skeleton** body have been imported, e.g. the rim is not needed in the **Housing** body 
* details which are independent from other bodies (such as the chamfer), were only defined in the **Housing** body

The **Separation bottom** body is created in a similar way:

<p align="center">
  <img src="./images/05-skeleton-body/separation-bottom.png" alt="Result" width="600">
</p>

As goes for **Separation top**:

<p align="center">
  <img src="./images/05-skeleton-body/separation-top.png" alt="Result" width="600">
</p>

With boolean operations and refined shapes, both halves look like:

<p align="center">
  <img src="./images/05-skeleton-body/housing-separated.png" alt="Result" width="500">
</p>

The proof of the pudding is in the eating. We change a few dimensions in the **sk front** sketch in the **Skeleton** body to see if the model is indeed parametric:

<p align="center">
  <img src="./images/05-skeleton-body/change-dimensions-front.png" alt="Result" width="500">
</p>

Indeed, the result is as expected:

<p align="center">
  <img src="./images/05-skeleton-body/result-of-change.png" alt="Result" width="500">
</p>

It appears that the wall of the bottom part is too thin to support the groove, so the inner wall of the groove is no longer there. The correction for this can be made in the same sketch:

<p align="center">
  <img src="./images/05-skeleton-body/correction-of-wall-thickness.png" alt="Result" width="500">
</p>

This effectively fixes the groove:

<p align="center">
  <img src="./images/05-skeleton-body/groove-repaired.png" alt="Result" width="500">
</p>

# Checking the model

## Checking links

It can sometimes (although rarely) occur that links between bodies cause errors that are very hard to find. Sometimes the problem is that there are crosslinks between bodies, i.e. body A refers to body B and body B refers back to body A. This circular reference causes FreeCAD to stop automatic recalculation of the part.

The dependency graph (menu Tools > Dependency Graph) can be very helpful to spot those errors. To use this tool, the third party software [Graphviz](https://graphviz.org/) needs to be installed (see [https://wiki.freecad.org/Std_DependencyGraph](https://wiki.freecad.org/Std_DependencyGraph)).

The dependency graph of the housing looks like this (text balloons were added manually):

![Dependency graph](./images/06-check-model/dependency-graph.svg)

The graph shows that:
* Bodies **Separation Top**, **Separation Bottom** and **Housing** all refer to the **Skeleton** body 
* Body **Housing top** refers to **Separation top** and **Housing**
* Body **Housing bottom** refers to **Separation bottom** and **Housing**
* Bodies **Housing bottom refined** and **Housing top refined** refer to **Housing bottom** and **Housing top** respectively
* References made by the **Part workbench** act on bodies, while references made by the **Part design workbench** act on features
* All arrows between the parts are black, indicating there are no errors in this graph

## Using the Check geometry tool

The Check geometry tool from the part workbench can be used to check if the 3D model is valid (Part workbench > Part > Check geometry ![Dependency graph](./images/06-check-model/check-geometry-button-small.png)). It is beyond the scope of this tutorial to explain how to solve common problems. MangoJelly has an [excellent video](https://www.youtube.com/watch?v=bw1Y5mrHrWY) on this tool. If causes are hard to find, the FreeCAD community is also willing to help out.

## Checking the result in the slicer

I'm using this technique often for 3D printing projects. One of the lessons I learned the hard way is that it is important to regularly check if the parts are printable.

Things to specifically pay attention to:
- are all details still large enough to print?
- would a different orientation of the separation plane make printing easier?
- is it possible to avoid support structures easily?
- is it possible to reduce print time by making other design choices?

<p align="center">
  <img src="./images/06-check-model/slicing.png" alt="Result" width="500">
</p>

As can be seen in this screenshot, both the top of the rim and the sides of the the groove are printale with multiple adjacent tracks. The dark blue lines indicate that the protrusion around the power connector is partially unsupported, but since these areas are very small, we will probably be fine.



# Creating references to the internal components of the housing

In the next example, we will build a housing for an internet of things application. The device will contain a thermometer/barometer/hygrometer connected to a microcontroller. The microcontroller can record the environmental conditions and report logging information over a wireless link.

For projects like this, it is important to obtain accurate 3D models. Usually they are available as STEP file or in another format which can be imported in FreeCAD.

Import the electronic components in the FreeCAD file and orient them well. In this project there is a risk that the heat of the wifi module of the microcontroller affects the temperature measurement of the sensor, so it is important to minimize thermal crosstalk when designing the housing.

<p align="center">
  <img src="./images/07-referencing-components/import-components.png" alt="Result" width="600">
</p>

Create the **Skeleton** body. In the skeleton, import important geometry of the components using shape binders. This way, the sketches in the skeleton will dynamically follow the components when the components are moved.

<p align="center">
  <img src="./images/07-referencing-components/references-to-components.png" alt="Result" width="600">
</p>

Create the sketches in the **Skeleton** body. 

<p align="center">
  <img src="./images/07-referencing-components/sketches-in-skeleton.png" alt="Result" width="600">
</p>

Create the **Housing**, **Separation top**, **Separation bottom**, **Housing top** and **Housing bottom** like in the previous example.

<p align="center">
  <img src="./images/07-referencing-components/final-housing-bottom.png" alt="Result" width="600">
</p>

<p align="center">
  <img src="./images/07-referencing-components/final-housing-total.png" alt="Result" width="600">
</p>

We can now move the boards around, and (within certain limits), the cavities in the housing will follow the components.


# Using self tapping screws to close the housing

I often use self tapping screws for these housings. With the right tolerances, these screws work really well and require no post processing (tapping, inserts) in the parts, which makes it quite fast. These screws are available from many different suppliers at AliExpress.

<p align="center">
  <img src="./images/08-self-tapping-screws/self-tapping-screws.png" alt="Screws" width="150">
</p>

In order to make the screw holes parametric, I created a model of the screw which contains an additional sketch representing the hole in the housing.

<p align="center">
  <img src="./images/08-self-tapping-screws/additional-sketch.svg" alt="Screws" width="600">
</p>

$\textcolor{red}{\textsf{:warning: In reality, these screws are not conical. Some day I will make a model that more closely resembles the shape of these screws. .}}$ 

## Creating a screw hole
This is how it works:

Insert screw in the model using File > Merge project
1. Create a shape binder **hs ref screw hole 1** in the **Housing** body, referencing the screw hole sketch from the model of the screw (no need to make an intermediate reference in the **Skeleton** body)
2. Make the model of the original screw invisible (so we can only select elements fro the shape binder)
3. Select three points on the shape binder of the hole, and create a datum plane **hs pln screw hole 1** through these points

<p align="center">
  <img src="./images/08-self-tapping-screws/create-datum-plane.png" alt="Screws" width="500">
</p>

4. Create a sketch **hs screw hole 1** on this datum plane, tracing one half of the screw hole
5. Add a construction geometry line to this sketch, representing the centerline of the screw. I usually make the length equal to an arbitrary other line of the sketch to make the sketch fully defined.

<p align="center">
  <img src="./images/08-self-tapping-screws/create-sketch.png" alt="Screws" width="500">
</p>

6. Create a Groove **HS Screw hole 1** based on this sketch, choosing the construction line as a centerline.

<p align="center">
  <img src="./images/08-self-tapping-screws/create-groove.png" alt="Screws" width="600">
</p>

Now if we move the screw to another location in x, y or z-direction, the shape binder **hs ref screw hole 1** and the datum plane **hs pln screw hole 1** will move with it, and thus the hole in the part will be fully parametric.

## Creating a pillar for the screw
It may occur that the seperation of the housing does not line up with the separation in the screw hole model. For instance, In the housing model I lined up the separation in the middle of the USB port, so the housing can be closed easily. 

To solve this, we can make a local pillar in the bottom housing and a hole in the top housing.

1. Create a shape binder **sk ref screw pillar 1** in the **Skeleton** body.
2. Make the model of the original screw invisible 
3. Create a datum plane **sk pln screw pillar 1** like we did in the housing
4. Create a sketch **sk screw pillar 1** that represents both the pillar in the **Bottom housing** and the hole in the **Top housing**. The top of the pillar must align with the separation plane in the screw hole, the bottom of the pillar is aligned with the lower line of the separation
5. Make **Separation bottom** the active body
6. Create a shape binder of **sk screw pillar 1** from the **Skeleton** body and rename it **sb ref screw pillar 1**
7. Create a datum plane **sb pln screw pillar 1** like we did in the housing
8. Create a sketch **sb screw pillar 1** to create the pillar, and add a geometry line that will be the center line of the pillar
9. Create a revolution and name it **SB Screw pillar 1**
5. Make **Separation top** the active body
6. Create a shape binder of **sk screw pillar 1** from the **Skeleton** body and rename it **st ref screw pillar 1**
7. Create a datum plane **st pln screw pillar 1** like we did in the housing
8. Create a sketch **st screw pillar 1** to create the hole for the pillar, and add a geometry line that will be the center line of the groove
9. Create a groove and name it **ST Screw pillar 1**


# Creating a complex hinge

# Creating references to external parts

