import asyncio
import aiohttp

async def get_rep(username):
    async with aiohttp.ClientSession() as session:
        async with session.get(f'https://api.github.com/users/{username}') as response:
            data = await response.json()
            repositories_url = data['repos_url']
            
            async with session.get(repositories_url) as response:
                repositories_data = await response.json()                
                repositories = [repo['full_name'] for repo in repositories_data]
                
                print(f"User: {username}")
                for repo in repositories:
                    print(repo)
                print()
                
users = ['Arantir1', 'EgorTimofeychik', 'maximax15', 'letov2110', 'denirix', 'Noowkies', 'NikDychek', 
         'marinamonit', 'PolonskyIllya', 'temabuchka88', 'LuydmilaKot', 'katherinepcholka', 'telenchenkosergey']

loop = asyncio.get_event_loop()
tasks = [get_rep(user) for user in users]
loop.run_until_complete(asyncio.gather(*tasks))
