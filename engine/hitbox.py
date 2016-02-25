import spriteObject

class Hitbox(spriteObject.RectSprite):
    def __init__(self,center,size,owner,hitbox_id=0):
        #Flip the distance from center if the fighter is facing the other way
        self.center = center
        if owner.facing == -1:
            self.center[0] = -self.center[0]
        spriteObject.RectSprite.__init__(self,[0,0],size,[255,0,0])
        self.rect.center = [owner.rect.center[0] + self.center[0], owner.rect.center[1] + self.center[1]]
        self.owner = owner
        self.hitbox_id = hitbox_id
        
    def onCollision(self,other):
        return
    
    def update(self):
        return

    def recenterSelfOnOwner(self):
        self.rect.topleft = [self.owner.rect.topleft[0] + self.topleft[0],
                             self.owner.rect.topleft[1] + self.topleft[1]]
        
    
class DamageHitbox(Hitbox):
    def __init__(self,center,size,owner,
                 damage,baseKnockback,knockbackGrowth,trajectory,
                 hitstun,hitbox_id):
        Hitbox.__init__(self,center,size,owner,hitbox_id)
        self.damage = damage
        self.baseKnockback = baseKnockback
        self.knockbackGrowth = knockbackGrowth
        self.trajectory = self.owner.getForwardWithOffset(trajectory)
        self.hitstun = hitstun
        
    def onCollision(self,other):
        if other.lockHitbox(self,self.hitstun):
            other.applyKnockback(self.damage, self.baseKnockback, self.knockbackGrowth, self.trajectory)
            print(other.damage)
        
    def update(self):
        Hitbox.update(self)
        self.recenterSelfOnOwner() 
        
class GrabHitbox(Hitbox):
    def __init__(self,center,size,owner,owner_action,other_action,hitbox_id):
        Hitbox.__init__(self,center,size,owner,hitbox_id)
        self.owner_action = owner_action
        self.other_action = other_action

    def onCollision(self,other):
        owner.setGrabbing(owner,other)
        
        try: 
            owner.changeAction(owner_action)
        except NameError:
            print "Grab hitbox " + hitbox_id + " from " + owner + " couldn't set owner's action to " + owner_action
            owner.doIdle()
            other.doIdle()
            return False
        try:
            other.changeAction(other_action)
        except NameError:
            print "Grab hitbox " + hitbox_id + " from " + owner + " couldn't set victim's action to " + other_action
            other.doIdle()
            other.doIdle()
            return False
        return True
            

    def update(self):
        Hitbox.update(self)
        self.recenterSelfOnOwner()

