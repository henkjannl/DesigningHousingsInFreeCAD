# Introduction
This tutorial I’ll demonstrate how to create 3D printed housings using FreeCAD. The advantage of this approach is that it is quite structured,
and you can manage changes in the design quite well, even if the design gets complex.

To follow this tutorial, you need to be familiar with the part design workbench and the sketcher. I’ll try to just focus on a high conceptal level.

# Topics in this document
- [Introduction](#introduction)
- [Topics in this document](#topics-in-this-document)
- [Concept of making a housing using boolean operation of bodies](#concept-of-making-a-housing-using-boolean-operation-of-bodies)
- [Making changes to the housing](#making-changes-to-the-housing)
- [Adding a groove in the top part and a rim in the bottom section](#adding-a-groove-in-the-top-part-and-a-rim-in-the-bottom-section)
- [Checking the result in the slicer](#checking-the-result-in-the-slicer)
- [Apply a workaround to ensure the colors remain the same](#apply-a-workaround-to-ensure-the-colors-remain-the-same)
- [Adding a connector hole to the housing](#adding-a-connector-hole-to-the-housing)
- [Using a skeleton to drive dimensions of the bodies](#using-a-skeleton-to-drive-dimensions-of-the-bodies)
- [Checking links between features using the dependency graph](#checking-links-between-features-using-the-dependency-graph)
- [Applying a naming convention for bodies and features](#applying-a-naming-convention-for-bodies-and-features)
- [Creating references to the internal components of the housing](#creating-references-to-the-internal-components-of-the-housing)
- [Using self tapping screws to close the housing](#using-self-tapping-screws-to-close-the-housing)
- [Creating a complex hinge](#creating-a-complex-hinge)
- [Creating references to external parts](#creating-references-to-external-parts)

# Concept of making a housing using boolean operation of bodies
I this example, we want to create a fairly complex housing which consists of two shells which can be assembled together.
1. We first create the complex housing (1) as a single body, without worrying about the separation.
2. We then create a second body (2) separation top, which covers which part of the housing needs to end up in the top half of the housing
3. We create a bottom separation (3) as a third body in the same way
4. Then we create the top housing as a boolean operation between the housing and the top separation
The general concept of this tutorial is to create a housing out of three bodies, and then use the boolean operator from the part workbench to 

![General concept](./images/01-concept/concept.png)

The housing is created as the first body named **Housing**, in this example it consists of an additive loft and a subtractive loft.

![Housing](./images/01-concept/housing.png)

Then we create another body in the same part, and we call it **Separation top**. In this example, it constists of a pad and an additive pipe that creates the rim. Not that the pad is deliberately larger than the housing.

![Separation top](./images/01-concept/separation-top.png)

We also create **Separation bottom** as a single body.

![Separation bottom](./images/01-concept/separation-bottom.png)

Next we move to the part workbench. We select **Housing** and **Separation top**, and choose the Intersection command from the toolbar.

![Housing top](./images/01-concept/housing-top.png)

A new body named **Common** is created, consisting of the boolean intersection of both selected bodies. We rename that part **Housing top**.

It may seem as if the **Housing** body has disappeared from the model tree, so we can no longer select it to create the bottom housing. However, if we expand the **Housing top** body, we can see that **Housing** is still there. We can now select the **Housing** body and the **Separation bottom** body and we can again apply the intersect tool on those two bodies. The resulting body is named **Common 001**. We rename it to **Housing bottom**.

![Housing bottom](./images/01-concept/housing-bottom.png)

After modifying the color and transparency of both housing parts, the result looks like this:

![Result](./images/01-concept/result.png)


# Making changes to the housing

# Adding a groove in the top part and a rim in the bottom section

# Checking the result in the slicer

# Apply a workaround to ensure the colors remain the same

# Adding a connector hole to the housing

# Using a skeleton to drive dimensions of the bodies

# Checking links between features using the dependency graph

# Applying a naming convention for bodies and features

# Creating references to the internal components of the housing

# Using self tapping screws to close the housing

# Creating a complex hinge

# Creating references to external parts
