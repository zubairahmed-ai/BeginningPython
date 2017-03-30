.meshgrid - done

.arrange - done

.ravel - done

zip - used to create iterables on lists and tuples

.newaxis

.hstack - done

.vstack - done

.range - done

getattr - gets attribute value

.map - uses a function over a enumerable and returns value (squares, range(10))

pd.concat

pd.cut - used to cut a dataframe into specified pieces for creating categories - train['CategoricalAge'] = pd.cut(train['Age'], 5)

pd.crosstab

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
