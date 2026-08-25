import socket



def listen(senderIP, port=80, do_on_answer=None, answerAmount=0,
           early_exit=None):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("", port))
        
        s.listen(5)
        
        
        output = []
        
        
        while True if answerAmount == 0 else answerAmount:
            c, addr = s.accept()
            
            if do_on_answer is not None:
                doOnAnswer(c, addr)
            else:
                output.append(s.recv(1024).decode())
            
            if answerAmount == 0:
                if early_exit(c, addr):
                    break
            
            else:
                answerAmount -= 1
    
    
    if do_on_answer is None:
        return output



def send(recieverIP, data, port=80):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((recieverIP, port))
        
        if data is str:
            data = data.encode("utf-8")
        
        s.send(data)

