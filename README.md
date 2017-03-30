.meshgrid - done

.arrange - done

.ravel - flattens an array

zip - used to create iterables on lists and tuples

.newaxis

.hstack - horizontally arranges a matrix

.vstack - vertically arranges a matrix

.range - specify range of values eg range(10)

getattr - gets attribute value

.map - uses a function over a enumerable and returns value (squares, range(10))

pd.concat

pd.cut - used to cut a dataframe into specified pieces for creating categories - train['CategoricalAge'] = pd.cut(train['Age'], 5)

pd.crosstab - uses to check the frequency of a value in another 
pd.crosstab[df.Survived, df. df.Pclass]

https://www.youtube.com/watch?v=4_VLxu41ffw
http://hamelg.blogspot.com/2015/11/python-for-data-analysis-part-19_17.html


df.loc - returns columns that we are interested in based on the criteria that we specify
example http://pythonjourney.com/python-pandas-dataframe-loc-my-understanding-so-far/

pd.qcut

np.random.randint


family[ 'Family_Single' ] = family[ 'FamilySize' ].map( lambda s : 1 if s == 1 else 0 )

def get_title(name):
	title_search = re.search(' ([A-Za-z]+)\.', name)
	# If the title exists, extract and return it.
	if title_search:
		return title_search.group(1)
	return ""
