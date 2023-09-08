import win32com.client
import os

qinfo = win32com.client.Dispatch("MSMQ.MSMQQUEUEInfo")
computer_name = os.geteve('COMPUTERNAME')
qinfo.FormatName = 'direct=os:'+computer_name+"\\PRIVATE$\\niru"
queue  = qinfo.Open(2,0)
msg = win32com.client.Dispatch("MSMQ.MSMQMessage")
msg.Label = "TestMsg"
msg.Body = "The quick brown fox jumps over the lazy dog"
msg.Send(queue)

queue.Close()