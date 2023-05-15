
### Documentation

Read the docs

### Queries

-   Top trending tags appearing in StackOverFlow in a given date range.
-   Top users in StackOverFlow based on different sort options in a given date range.




### Top trending tags appearing in StackOverFlow
#### Command Line Arguments.

order_by = desc (default), asc.
sort_by = popular (default), activity, name.

Definition.
popular - count.
activity - the creation_date of the last question asked with the tag.
name - name.

```py

top-trending-tags-appearing-in-StackOverFlow.py -order_by 'desc' -sort_by 'popular' -from_date '2023-05-01' -to_date '2023-05-15' 

```

#### Top users in StackOverFlow
#### Command Line Arguments.

order_by = desc (default), asc.
sort_by = reputation (default), creation, modified, name.

Definition.
reputation - reputation.
creation - creation_date.
name - display_name.
modified - last_modified_date.

```py

top-users-in-StackOverFlow.py -order_by 'desc' -sort_by 'reputation' -from_date '2023-05-01' -to_date '2023-05-15' 

```