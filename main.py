

linkedlist  l = new linkedlist()

l.add(1)
l.add(2)

--------
l.add(3)


....

linkedlist(){
    self.first = null #el primer nodo 

}



public void add(value){

   if( not self.first ){
       self.first = new Node(value)
   }
   else{
        currentNode = self.first

        # ir hasta el ultimo nodo
        while( currentNode.next ){
            currentNode = currentNode.next 
        }

        #que va pasar cuando estes en el ultimo nodo
        currentNode.next = new Node(value)

   }

}

removerElultimo

buscar

remover por valor

remover por posicion 

pop {
    node = self.first
    self.first = self.first.next
    return node
}

