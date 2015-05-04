import requests
import json
data_url = 'http://www.compjour.org/files/code/json-examples/nyt-books-bestsellers-hardcover-fiction.json'
data = json.loads(requests.get(data_url).text)
books = data['results']['books']

print('A.', len([b for b in books if b['publisher'] == "Scribner"]))


print('B.', len([b for b in books if "detective" in b['description'].lower()]))


from operator import itemgetter
x = max(books, key = itemgetter('weeks_on_list'))
print('C.', '%s|%s' % (x['title'], x['weeks_on_list']))


x = max(books, key = itemgetter('rank_last_week'))
print('D.', '%s|%s|%s' % (x['title'], x['rank'], x['rank_last_week']))


books_unranked_last_week = [b for b in books if b['rank_last_week'] == 0]
print('E.', len(books_unranked_last_week))


x = min(books_unranked_last_week, key = itemgetter('rank'))
print('F.', '%s|%s' % (x['title'], x['rank']))


books_ranked_last_week = [b for b in books if b['rank_last_week'] > 0]
# define a helper function
def calc_rank_change(book_obj):
    return book_obj["rank_last_week"] - book_obj["rank"]

x = max(books_ranked_last_week, key = calc_rank_change)
s = "|".join([x['title'], str(x['rank']), str(calc_rank_change(x))])
print("G.", s)


x = min(books_ranked_last_week, key = calc_rank_change)
s = "|".join([x['title'], str(x['rank']), str(calc_rank_change(x))])
print("H.", s)


changes = [calc_rank_change(b) for b in books_ranked_last_week]
x = [v for v in changes if v > 0]
s = sum(x)
print("I.", s)

changes = [calc_rank_change(b) for b in books_ranked_last_week]
x = [v for v in changes if v < 0]
s = sum(x)
print("J.", "%s|%s" % (len(x), s))


print('K.', max([len(b['title']) for b in books]))


x = round(sum([len(b['title']) for b in books]) / len(books))
print('L.', x)
        
