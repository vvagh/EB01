import json

sourceFile = open('corpus.json', 'r')
json_data = json.load(sourceFile)

query_list = ['world interest rates table', '2008 beijing olympics', 'fast cars', 'clothing sizes', 'phases of the moon',
              'usa population by state', 'prime ministers of england', 'ipod models', 'bittorrent clients',
              'olympus digital slrs', 'composition of the sun', 'running shoes', 'fuel consumption',
              'stock quote tables', 'top grossing movies', 'nutrition values',
              'state capitals and largest cities in us', 'professional wrestlers', 'company income statements',
              'dog breeds', 'ibanez guitars', 'used cellphones', 'world religions', 'stocks', 'academy awards',
              '2008 olympic gold medal winners', 'currencies of different countries', 'science discoveries',
              'pga leaderboard', 'pain medications', 'football clubs city', 'healthy food cost', 'capitals attractions',
              'diseases mortality', 'cigarette brands market share', 'apples market share',
              'healthy food nutritional value', 'hormones effects', 'household chemicals strength', 'lakes altitude',
              'laptops cpu', 'asian countries currency', 'diseases risks', 'external drives capacity',
              'baseball teams captain', 'maryland counties population', 'countries capital', 'diseases incidence',
              'eu countries year joined', 'irish counties area', 'cereals nutritional value', 'erp systems price',
              'cats life span', 'broadway musicals director', 'infections treatment', 'food type',
              'board games number of players', 'google products reviews', 'constellations closest constellation',
              'games age']

fname = 'STR.txt'

with open(fname) as f:
    content = f.readlines()
tableId = []
for line in content:
    sline = line.split()
    tid = sline[2]
    table_id = [tid]
    tableId.append(table_id)

fname1 = 'qrels.txt'
with open(fname1) as f:
    content = f.readlines()
qrel = []
for line in content:
    sline = line.split()
    q_rel = sline[3]
    qrel.append(q_rel)
