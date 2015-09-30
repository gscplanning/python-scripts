Accessing layers from geodatabases or from folder directories is pretty straightforward. SDE isn't as straightforward. Here are some common templates to use when accessing SDE tables for use in Python:

## Feature class at a version's root level

`"Database Connections\\<name of version>.sde\\Production.SDEDBO.<name of feature class>"`

## Feature class in a feature dataset

`"Database Connections\\<name of version>.sde\\Production.SDEDBO.<name of feature dataset>\\Production.SDEDBO.<name of feature class>"`

## From the raster database

`"Database Connections\\raster.sde\\Raster.SDEDBO.<name of raster dataset>"`
