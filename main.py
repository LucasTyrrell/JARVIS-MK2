from agent import spotify_agent,main_thread
from tokens import scheduler, refresh_tokens


#refresh the spotify api tokens, and then set them to be refreshed every hour
refresh_tokens()
scheduler.start()

#simple text based query loop for now
def chat():
    print("Awaiting query:")
    query = input()
    result = spotify_agent.invoke(
        {"messages": [{"role": "user", "content": query}]},
        config= main_thread
    )
    print(result["messages"][-1].content)


while True:
    chat()