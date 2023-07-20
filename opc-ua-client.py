import asyncio
import logging
from asyncua import Client, Node, ua

url = 'opc.tcp://192.168.1.5:4840'
namespace = ''

async def main():

    print(f'Connecting to {url} ...')
    async with Client(url=url) as client:
        # Find the namespace index to address custom objects
        nsidx = await client.get_namespace_index(namespace)
        print(f'Namespace Index for "{namespace}": {nsidx}')

        # Get the variable node for read / write
        var = await client.nodes.root.get_child(
            ['0:Objects', f'{nsidx}:MyObject', f'{nsidx}:MyVariable']
        )
        value = await var.read_value()
        print(f'Value of MyVariable ({var}): {value}')

        new_value = value - 50
        print(f'Setting value of MyVariable to {new_value} ...')
        await var.write_value(new_value)

        # Calling a method
        res = await client.nodes.objects.call_method(f'{nsidx}:ServerMethod', 5)
        print(f'Calling ServerMethod returned {res}')

# logger = logging.getLogger('asyncua')
# logging.disable(logging.WARNING)

# data_variables = ['direction', 'speed', 'machine_details']

# async def dict_format(keys, values):
#     return dict(zip(keys, values))

# async def main():
#     while True:
#         url = ''
#         async with Client(url=url) as client:
#             data_list = []
#             namespace = 'mynamespace'
#             idx = await client.get_namespace_index(namespace)
#             for i in range(len(data_variables)):
#                 myvar = await client.nodes.root.get_child(['0:Objects', '{}:vPLC'.format(idx), '{}:{}'.format(idx,data_variables[i])])
#                 val = await myvar.get_value()
#                 data_list.append(val)
#             print(await dict_format(data_variables, data_list))
#             await asyncio.sleep(5)

if __name__ == '__main__':
    asyncio.run(main())
