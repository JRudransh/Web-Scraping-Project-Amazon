from requests_html import HTMLSession
session = HTMLSession()

search_name = 'samsung'
url = f'https://www.amazon.in/s?k={search_name}'

r = session.get(url)
data_list = r.html.find('.s-card-container')

# For the first time
# with open('db.txt', 'w') as f:
#     for data in data_list:
#         title = data.find('.a-text-normal')[0].text
#         f.write(f'{title}\n')


# Read data
with open('db.txt', 'r') as f:
    data_list_read = f.readlines()

old_data_list = []
for data in data_list_read:
    old_data_list.append(data.replace('\n', ''))

# print(old_data_list)

# compare data
new_data_list = []
for data in data_list:
    title = data.find('.a-text-normal')[0].text
    new_data_list.append(title)

# print(new_data_list)
# print(old_data_list)

# Compare here
new = []
removed = []
all_data = list(set(new_data_list).union(set(old_data_list)))

for data in all_data:
    if (data in new_data_list) and (data not in old_data_list):
        print('REMOVED:', end='\t')
        print(data)
        removed.append(data)
    elif (data not in new_data_list) and (data in old_data_list):
        print('NEW:', end='\t')
        print(data)
        new.append(data)


# Update in database
with open('db.txt', 'w') as f:
    for data in new_data_list:
        f.write(f'{data}\n')


print(f'Found {len(new)} new data & {len(removed)} data Removed.')
