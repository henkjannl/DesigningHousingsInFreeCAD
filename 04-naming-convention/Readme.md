* [Up to "Table of contents"](../README.md)
* [Back to "3 Retaining the colors of both housing bodies"](../03-Retaining-colors/Readme.md)
* [Next to "5 Using a skeleton to drive dimensions of the bodies"](../05-skeleton-body/Readme.md)

# 4 Applying a naming convention

As the number of bodies and features expands, identifying features becomes progressively complex. To mitigate this, it is helpful to adopt distinct and meaningful names for features. I have devised a systematic naming approach, outlined as follows:

**Non-volumetric features**

I use lowercase for non-volumetric features such as sketches and datum planes in the following format:

`bb ttt nnnnn eee`

where:

| <!-- --> | <!-- -->                                                                                                             |
|----------|----------------------------------------------------------------------------------------------------------------------|
| `bb`     | A unique abbreviation of the body (`hs` for housing, `st` for separation top, `sb` for separation bottom, etc.)      |
| `ttt`    | An optional 3 letter code for the type of feature: <br> - `pln` for a plane <br> - `axs` for an axis <br> - `ref` for a shape binder |
| `nnnnn`  | The name of the feature                                                                                              |
| `eee`    | Optional extension for additive and subtractive pipes: <br>  - the trajectory of the pipe is followed by `trj` <br>  - the cross section is followed by `crs` |


**Volumetric features**

For volumetric features, such as pads, cuts and revolves, I use Sentence case:

`Bb Nnnnn`

where:

| <!-- --> | <!-- -->                                                                                                             |
|----------|----------------------------------------------------------------------------------------------------------------------|
| `BB`     | A unique abbreviation of the body (`HS` for housing, `ST` for separation top, `SB` for separation bottom, etc.)      |
| `Nnnnn`  | The name of the feature                                                                                              |

Often, the last sketch to define a volumetric feature has the same name as the volumetric feature, but they become distinct by the use of different case (e.g., a sketch may be named **hs base**, and the pad that is created using that sketch is named **HS Base**)

It is helpful to choose a pragmatic approach: for simple projects, the overhead of renaming every feature may not be worth the effort.


**Examples**
| <!-- -->            | <!-- -->                                                                                |
|---------------------|-----------------------------------------------------------------------------------------|
| `sk top`            | Top view sketch of the part in the **Skeleton** body                                    |
| `hs ref top`        | Shape binder in the **Housing** body, referencing the top view in the **Skeleton** body |
| `hs pln bottom`     | Datum plane in the **Housing** body, representing the bottom of this body               |
| `sb groove crs`     | Cross section of the groove in the **Separation bottom** body                           |
| `sb groove trj`     | Trajectory of the groove in the **Separation bottom** body                              |
| `SB Groove`         | The groove created as a pipe from `sb groove crs` and `sb groove trj`                   |


* [Up to "Table of contents"](../README.md)
* [Back to "3 Retaining the colors of both housing bodies"](../03-Retaining-colors/Readme.md)
* [Next to "5 Using a skeleton to drive dimensions of the bodies"](../05-skeleton-body/Readme.md)
