
class Animal:
    def __init__(self,name,pop,growth):
        self.name = name
        self.population = pop;
        self.growthConstant = growth
        
        self.predators = []
        self.prey = []
        self.relations = Relations()
        
    def getName(self):
        return self.name
    
    def getPopulation(self):
        return self.population
        
    def addPredator(self,pred,pval):
        self.predators.append(pred)
        self.relations.addRelation(pred,pval)
        
    def addPrey(self,prey,pval):
        self.prey.append(prey)
        self.relations.addRelation(prey,pval)
        
    def singleEulerSim(self,dt):
        k = self.growthConstant
        P = self.population
        preds = self.predators
        prey = self.prey
        relations = self.relations
        
        growth = k*P
        
        predation = 0
        for predator in preds:
            pr = relations.get(predator)
            pval = pr.getPredationConstant() 
            effect = -pval * predator.getPopulation() * P
            predation -= effect
            
        consumption = 0
        for pry in prey:
            pr = relations.get(pry)
            pval = pr.getPredationConstant()
            effect = pval * pry.getPopulation() * P
            consumption += effect

        deriv = growth - predation + consumption
        change = deriv * dt
        self.population += change
        
class Relation:
    def __init__(self,animal,pval):
        self.animal = animal
        self.pval = pval
        
    def getAnimal(self):
        return self.animal
        
    def getPredationConstant(self):
        return self.pval
    
    def __repr__(self):
        return self.animal
        
class Relations:
    def __init__(self):
        self.relations = []
        
    def addRelation(self,animal,pval):
        new = Relation(animal,pval)
        self.relations.append(new)
        
    def get(self,animal):
        rels = self.relations
        
        for rel in rels:
            rani = rel.getAnimal()
            if rani.getName() == animal.getName():
                return rel
        
        return None
        
class PredatorPreyModel:
    def __init__(self):
        self.animals = []
        
    def addAnimal(self,name,pop = 100, growth = .1):
        a = Animal(name,pop,growth)
        self.animals.append(a)
        return a
    
    def setPredator(self,pred,prey,pred_k,prey_k):
        pred.addPrey(prey,pred_k)
        prey.addPredator(pred,prey_k)
    
    def euler(self,itters, dt):
        data = [[0],[]]
        for animal in self.animals:
            data[1].append([animal.getPopulation()])
        print(data)
        for i in range(itters):
            data[0].append(data[0][-1]+dt)
            for j in range(len(self.animals)):
                animal = self.animals[j]
                animal.singleEulerSim(dt)
                data[1][j].append(animal.getPopulation())
                
        return data
        
if __name__ == "__main__":
    model = PredatorPreyModel()
    r = model.addAnimal('Rabbit',50,.1)
    f = model.addAnimal('Fox',15,-.05)
    
    print(r.getPopulation())
    print(f.getPopulation())
    
    model.setPredator(f,r,.001,.01)
    data = model.euler(100,1)
    print(data)
    
    print(r.getPopulation())
    print(f.getPopulation())