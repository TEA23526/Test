devices=["R1","R2","R3","S1","S2"] 
switche=[]
ruter=[]
for item in devices: 
    
    if "S" in item:
        switche.append(item)
        print(item) 
    elif "R" in item:
        ruter.append(item)

print(f"meine Scitche: {switche}")
print(f"Meine Ruter: {ruter}")