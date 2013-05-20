
class Animal:
    def __init__(self,name,pop,growth):
        self.type = name
        self.population = pop;
        self.growthConstant = growth
        
        self.predators = []
        self.prey = []
        
class Relation:
    def __init__(self,predator,prey,pred_k,prey_k):
        self.predator = predator
        self.prey = prey
        self.pred_k = pred_k
        self.prey_k = prey_k
        
class PredatorPreyModel:
    def __init__(self):
        self.animals = []
        self.relations = []
        self.deltaT = 1
        
    def addAnimal(self,name,pop = 100, growth = .1):
        a = Animal(type,pop,growth)
        self.animals.append(a)
        return a
    
    def addRelation(self):
        pass
    
    def setPredator(self,pred,prey,pred_k,prey_k):
        r = Relation(pred,prey,pred_k,prey_k)
        self.relations.append(r)
        return r
    
    def euler(self):
        pass
        
if __name__ == "__main__":
    model = PredatorPreyModel()
    r = model.addAnimal('Rabbit',200,.2)
    f = model.addAnimal('Fox',100,-.1)
    
    model.setPredator(f,r,.2,.1)