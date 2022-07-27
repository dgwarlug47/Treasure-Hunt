from components import Movement, ReceiverAction, ReceiverState

def policyUI(receiverActionManagement, senderInputSize):
    gridSize = 5
    assert(type(receiverActionManagement.actions[0]) == ReceiverAction)

    for senderInput in range(1, senderInputSize + 1):
        print("message = " + str(senderInput))
        ans = ""
        for y in range(gridSize):
            for x in range(gridSize):
                state = ReceiverState(x, y, senderInput)
                action = receiverActionManagement.bestAction(state)
                if (action.movement == Movement.up):
                    ans += 'U'
                elif (action.movement == Movement.down):
                    ans += 'D'
                elif (action.movement == Movement.left):
                    ans += 'L'
                elif (action.movement == Movement.right):
                    ans += 'R'
                else:
                    assert(False)
                ans += '|'
            ans += '|'
        print(ans)


