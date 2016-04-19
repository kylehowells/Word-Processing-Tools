# Import Words into SQLite


Create a SQLite file.

```bash
sqlite3 words.db
```

### sqlite3 Commands

Create the table to put the data in.

```sql
create table words(word text PRIMARY KEY, count INTEGER);
```

Setup sqlite3 for the import

```sql
.mode list
.separator " "
```

Import the data

```sql
.import "../UNIX_style/filepath/wordfrequency.txt" words
```

Explore the data

```sql
select count(*) from words;
.headers on
.mode column
select * from words order by words.count DESC limit 20;
```

Example output

```
word        count
----------  ----------
the         791445
of          404178
and         311101
in          271917
to          226011
a           202161
is          108721
as          97457
was         91648
by          77499
for         76042
s           75032
that        74823
with        68988
on          65228
from        52991
are         52302
it          46270
his         45334
at          40027
```
