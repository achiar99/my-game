from collections import Counter
from typing import List

from .noble_tile import NobleTile
from .development_card import DevelopmentCard
from .resource import Resources


def get_all_first_level_development_cards() -> List[DevelopmentCard]:
    cards: List[DevelopmentCard] = []
    # ONYX
    cards.append(DevelopmentCard(level=1, gift=Resources.ONYX, score=0, cost=Counter({Resources.DIAMOND: 1,
                                                                                      Resources.EMERALD: 1,
                                                                                      Resources.ONYX: 0,
                                                                                      Resources.RUBY: 1,
                                                                                      Resources.SAPPHIRE: 1})))
    cards.append(DevelopmentCard(level=1, gift=Resources.ONYX, score=0, cost=Counter({Resources.DIAMOND: 1,
                                                                                      Resources.EMERALD: 1,
                                                                                      Resources.ONYX: 0,
                                                                                      Resources.RUBY: 1,
                                                                                      Resources.SAPPHIRE: 2})))
    cards.append(DevelopmentCard(level=1, gift=Resources.ONYX, score=0, cost=Counter({Resources.DIAMOND: 0,
                                                                                      Resources.EMERALD: 1,
                                                                                      Resources.ONYX: 0,
                                                                                      Resources.RUBY: 1,
                                                                                      Resources.SAPPHIRE: 2})))
    cards.append(DevelopmentCard(level=1, gift=Resources.ONYX, score=0, cost=Counter({Resources.DIAMOND: 0,
                                                                                      Resources.EMERALD: 1,
                                                                                      Resources.ONYX: 1,
                                                                                      Resources.RUBY: 3,
                                                                                      Resources.SAPPHIRE: 0})))                                    
    cards.append(DevelopmentCard(level=1, gift=Resources.ONYX, score=0, cost=Counter({Resources.DIAMOND: 0,
                                                                                      Resources.EMERALD: 2,
                                                                                      Resources.ONYX: 0,
                                                                                      Resources.RUBY: 1,
                                                                                      Resources.SAPPHIRE: 0})))
    cards.append(DevelopmentCard(level=1, gift=Resources.ONYX, score=0, cost=Counter({Resources.DIAMOND: 2,
                                                                                      Resources.EMERALD: 2,
                                                                                      Resources.ONYX: 0,
                                                                                      Resources.RUBY: 0,
                                                                                      Resources.SAPPHIRE: 0})))
    cards.append(DevelopmentCard(level=1, gift=Resources.ONYX, score=0, cost=Counter({Resources.DIAMOND: 0,
                                                                                      Resources.EMERALD: 3,
                                                                                      Resources.ONYX: 0,
                                                                                      Resources.RUBY: 0,
                                                                                      Resources.SAPPHIRE: 0})))        
    cards.append(DevelopmentCard(level=1, gift=Resources.ONYX, score=1, cost=Counter({Resources.DIAMOND: 0,
                                                                                      Resources.EMERALD: 0,
                                                                                      Resources.ONYX: 0,
                                                                                      Resources.RUBY: 0,
                                                                                      Resources.SAPPHIRE: 4})))
    # SAPPHIRE
    cards.append(DevelopmentCard(level=1, gift=Resources.SAPPHIRE, score=0, cost=Counter({Resources.DIAMOND: 1,
                                                                                          Resources.EMERALD: 1,
                                                                                          Resources.ONYX: 1,
                                                                                          Resources.RUBY: 1,
                                                                                          Resources.SAPPHIRE: 0})))    
    cards.append(DevelopmentCard(level=1, gift=Resources.SAPPHIRE, score=0, cost=Counter({Resources.DIAMOND: 1,
                                                                                          Resources.EMERALD: 1,
                                                                                          Resources.ONYX: 1,
                                                                                          Resources.RUBY: 2,
                                                                                          Resources.SAPPHIRE: 0})))                                                                                                                                                                                                                                      
    cards.append(DevelopmentCard(level=1, gift=Resources.SAPPHIRE, score=0, cost=Counter({Resources.DIAMOND: 1,
                                                                                          Resources.EMERALD: 2,
                                                                                          Resources.ONYX: 0,
                                                                                          Resources.RUBY: 2,
                                                                                          Resources.SAPPHIRE: 0}))) 
    cards.append(DevelopmentCard(level=1, gift=Resources.SAPPHIRE, score=0, cost=Counter({Resources.DIAMOND: 0,
                                                                                          Resources.EMERALD: 3,
                                                                                          Resources.ONYX: 0,
                                                                                          Resources.RUBY: 1,
                                                                                          Resources.SAPPHIRE: 1})))  
    cards.append(DevelopmentCard(level=1, gift=Resources.SAPPHIRE, score=0, cost=Counter({Resources.DIAMOND: 1,
                                                                                          Resources.EMERALD: 0,
                                                                                          Resources.ONYX: 2,
                                                                                          Resources.RUBY: 0,
                                                                                          Resources.SAPPHIRE: 0})))     
    cards.append(DevelopmentCard(level=1, gift=Resources.SAPPHIRE, score=0, cost=Counter({Resources.DIAMOND: 0,
                                                                                          Resources.EMERALD: 2,
                                                                                          Resources.ONYX: 2,
                                                                                          Resources.RUBY: 0,
                                                                                          Resources.SAPPHIRE: 0})))
    cards.append(DevelopmentCard(level=1, gift=Resources.SAPPHIRE, score=0, cost=Counter({Resources.DIAMOND: 0,
                                                                                          Resources.EMERALD: 0,
                                                                                          Resources.ONYX: 3,
                                                                                          Resources.RUBY: 0,
                                                                                          Resources.SAPPHIRE: 0})))
    cards.append(DevelopmentCard(level=1, gift=Resources.SAPPHIRE, score=1, cost=Counter({Resources.DIAMOND: 0,
                                                                                          Resources.EMERALD: 0,
                                                                                          Resources.ONYX: 0,
                                                                                          Resources.RUBY: 4,
                                                                                          Resources.SAPPHIRE: 0})))  
    # EMERALD
    cards.append(DevelopmentCard(level=1, gift=Resources.EMERALD, score=0, cost=Counter({Resources.DIAMOND: 2,
                                                                                         Resources.EMERALD: 0,
                                                                                         Resources.ONYX: 0,
                                                                                         Resources.RUBY: 0,
                                                                                         Resources.SAPPHIRE: 1})))    
    cards.append(DevelopmentCard(level=1, gift=Resources.EMERALD, score=0, cost=Counter({Resources.DIAMOND: 0,
                                                                                         Resources.EMERALD: 0,
                                                                                         Resources.ONYX: 0,
                                                                                         Resources.RUBY: 2,
                                                                                         Resources.SAPPHIRE: 2})))                                                                                                                                                                                                                                      
    cards.append(DevelopmentCard(level=1, gift=Resources.EMERALD, score=0, cost=Counter({Resources.DIAMOND: 1,
                                                                                         Resources.EMERALD: 1,
                                                                                         Resources.ONYX: 0,
                                                                                         Resources.RUBY: 0,
                                                                                         Resources.SAPPHIRE: 3}))) 
    cards.append(DevelopmentCard(level=1, gift=Resources.EMERALD, score=0, cost=Counter({Resources.DIAMOND: 1,
                                                                                         Resources.EMERALD: 0,
                                                                                         Resources.ONYX: 1,
                                                                                         Resources.RUBY: 1,
                                                                                         Resources.SAPPHIRE: 1})))  
    cards.append(DevelopmentCard(level=1, gift=Resources.EMERALD, score=0, cost=Counter({Resources.DIAMOND: 1,
                                                                                         Resources.EMERALD: 0,
                                                                                         Resources.ONYX: 2,
                                                                                         Resources.RUBY: 1,
                                                                                         Resources.SAPPHIRE: 1})))     
    cards.append(DevelopmentCard(level=1, gift=Resources.EMERALD, score=0, cost=Counter({Resources.DIAMOND: 0,
                                                                                         Resources.EMERALD: 0,
                                                                                         Resources.ONYX: 0,
                                                                                         Resources.RUBY: 3,
                                                                                         Resources.SAPPHIRE: 0})))
    cards.append(DevelopmentCard(level=1, gift=Resources.EMERALD, score=0, cost=Counter({Resources.DIAMOND: 0,
                                                                                         Resources.EMERALD: 0,
                                                                                         Resources.ONYX: 2,
                                                                                         Resources.RUBY: 2,
                                                                                         Resources.SAPPHIRE: 1})))
    cards.append(DevelopmentCard(level=1, gift=Resources.EMERALD, score=1, cost=Counter({Resources.DIAMOND: 0,
                                                                                         Resources.EMERALD: 0,
                                                                                         Resources.ONYX: 4,
                                                                                         Resources.RUBY: 0,
                                                                                         Resources.SAPPHIRE: 0})))
    # RUBY
    cards.append(DevelopmentCard(level=1, gift=Resources.RUBY, score=0, cost=Counter({Resources.DIAMOND: 3,
                                                                                      Resources.EMERALD: 0,
                                                                                      Resources.ONYX: 0,
                                                                                      Resources.RUBY: 0,
                                                                                      Resources.SAPPHIRE: 1})))    
    cards.append(DevelopmentCard(level=1, gift=Resources.RUBY, score=0, cost=Counter({Resources.DIAMOND: 1,
                                                                                      Resources.EMERALD: 0,
                                                                                      Resources.ONYX: 3,
                                                                                      Resources.RUBY: 1,
                                                                                      Resources.SAPPHIRE: 0})))                                                                                                                                                                                                                                      
    cards.append(DevelopmentCard(level=1, gift=Resources.RUBY, score=0, cost=Counter({Resources.DIAMOND: 0,
                                                                                      Resources.EMERALD: 1,
                                                                                      Resources.ONYX: 0,
                                                                                      Resources.RUBY: 0,
                                                                                      Resources.SAPPHIRE: 2}))) 
    cards.append(DevelopmentCard(level=1, gift=Resources.RUBY, score=0, cost=Counter({Resources.DIAMOND: 2,
                                                                                      Resources.EMERALD: 1,
                                                                                      Resources.ONYX: 2,
                                                                                      Resources.RUBY: 0,
                                                                                      Resources.SAPPHIRE: 0})))  
    cards.append(DevelopmentCard(level=1, gift=Resources.RUBY, score=0, cost=Counter({Resources.DIAMOND: 2,
                                                                                      Resources.EMERALD: 1,
                                                                                      Resources.ONYX: 1,
                                                                                      Resources.RUBY: 0,
                                                                                      Resources.SAPPHIRE: 1})))     
    cards.append(DevelopmentCard(level=1, gift=Resources.RUBY, score=0, cost=Counter({Resources.DIAMOND: 1,
                                                                                      Resources.EMERALD: 1,
                                                                                      Resources.ONYX: 1,
                                                                                      Resources.RUBY: 0,
                                                                                      Resources.SAPPHIRE: 1})))
    cards.append(DevelopmentCard(level=1, gift=Resources.RUBY, score=0, cost=Counter({Resources.DIAMOND: 2,
                                                                                      Resources.EMERALD: 0,
                                                                                      Resources.ONYX: 0,
                                                                                      Resources.RUBY: 2,
                                                                                      Resources.SAPPHIRE: 0})))
    cards.append(DevelopmentCard(level=1, gift=Resources.RUBY, score=1, cost=Counter({Resources.DIAMOND: 4,
                                                                                      Resources.EMERALD: 0,
                                                                                      Resources.ONYX: 0,
                                                                                      Resources.RUBY: 0,
                                                                                      Resources.SAPPHIRE: 0})))
    # DIAMOND
    cards.append(DevelopmentCard(level=1, gift=Resources.DIAMOND, score=0, cost=Counter({Resources.DIAMOND: 0,
                                                                                         Resources.EMERALD: 2,
                                                                                         Resources.ONYX: 1,
                                                                                         Resources.RUBY: 0,
                                                                                         Resources.SAPPHIRE: 2})))    
    cards.append(DevelopmentCard(level=1, gift=Resources.DIAMOND, score=0, cost=Counter({Resources.DIAMOND: 0,
                                                                                         Resources.EMERALD: 0,
                                                                                         Resources.ONYX: 1,
                                                                                         Resources.RUBY: 2,
                                                                                         Resources.SAPPHIRE: 0})))                                                                                                                                                                                                                                      
    cards.append(DevelopmentCard(level=1, gift=Resources.DIAMOND, score=0, cost=Counter({Resources.DIAMOND: 0,
                                                                                         Resources.EMERALD: 1,
                                                                                         Resources.ONYX: 1,
                                                                                         Resources.RUBY: 1,
                                                                                         Resources.SAPPHIRE: 1}))) 
    cards.append(DevelopmentCard(level=1, gift=Resources.DIAMOND, score=0, cost=Counter({Resources.DIAMOND: 0,
                                                                                         Resources.EMERALD: 0,
                                                                                         Resources.ONYX: 0,
                                                                                         Resources.RUBY: 0,
                                                                                         Resources.SAPPHIRE: 3})))  
    cards.append(DevelopmentCard(level=1, gift=Resources.DIAMOND, score=0, cost=Counter({Resources.DIAMOND: 0,
                                                                                         Resources.EMERALD: 2,
                                                                                         Resources.ONYX: 0,
                                                                                         Resources.RUBY: 0,
                                                                                         Resources.SAPPHIRE: 2})))     
    cards.append(DevelopmentCard(level=1, gift=Resources.DIAMOND, score=0, cost=Counter({Resources.DIAMOND: 0,
                                                                                         Resources.EMERALD: 2,
                                                                                         Resources.ONYX: 1,
                                                                                         Resources.RUBY: 1,
                                                                                         Resources.SAPPHIRE: 1})))
    cards.append(DevelopmentCard(level=1, gift=Resources.DIAMOND, score=0, cost=Counter({Resources.DIAMOND: 3,
                                                                                         Resources.EMERALD: 0,
                                                                                         Resources.ONYX: 1,
                                                                                         Resources.RUBY: 0,
                                                                                         Resources.SAPPHIRE: 1})))
    cards.append(DevelopmentCard(level=1, gift=Resources.DIAMOND, score=1, cost=Counter({Resources.DIAMOND: 0,
                                                                                         Resources.EMERALD: 4,
                                                                                         Resources.ONYX: 0,
                                                                                         Resources.RUBY: 0,
                                                                                         Resources.SAPPHIRE: 0})))                                                                                                                                                                                                                                                                                                                      
    return cards


def get_all_second_level_development_cards() -> List[DevelopmentCard]:
    cards: List[DevelopmentCard] = []
    # ONYX
    cards.append(DevelopmentCard(level=2, gift=Resources.ONYX, score=1, cost=Counter({Resources.DIAMOND: 3,
                                                                                      Resources.EMERALD: 2,
                                                                                      Resources.ONYX: 0,
                                                                                      Resources.RUBY: 0,
                                                                                      Resources.SAPPHIRE: 2})))
    cards.append(DevelopmentCard(level=2, gift=Resources.ONYX, score=1, cost=Counter({Resources.DIAMOND: 3,
                                                                                      Resources.EMERALD: 3,
                                                                                      Resources.ONYX: 2,
                                                                                      Resources.RUBY: 0,
                                                                                      Resources.SAPPHIRE: 0})))                                    
    cards.append(DevelopmentCard(level=2, gift=Resources.ONYX, score=2, cost=Counter({Resources.DIAMOND: 0,
                                                                                      Resources.EMERALD: 4,
                                                                                      Resources.ONYX: 0,
                                                                                      Resources.RUBY: 2,
                                                                                      Resources.SAPPHIRE: 1})))
    cards.append(DevelopmentCard(level=2, gift=Resources.ONYX, score=2, cost=Counter({Resources.DIAMOND: 5,
                                                                                      Resources.EMERALD: 0,
                                                                                      Resources.ONYX: 0,
                                                                                      Resources.RUBY: 0,
                                                                                      Resources.SAPPHIRE: 0})))
    cards.append(DevelopmentCard(level=2, gift=Resources.ONYX, score=2, cost=Counter({Resources.DIAMOND: 0,
                                                                                      Resources.EMERALD: 5,
                                                                                      Resources.ONYX: 0,
                                                                                      Resources.RUBY: 3,
                                                                                      Resources.SAPPHIRE: 0})))        
    cards.append(DevelopmentCard(level=2, gift=Resources.ONYX, score=3, cost=Counter({Resources.DIAMOND: 0,
                                                                                      Resources.EMERALD: 0,
                                                                                      Resources.ONYX: 6,
                                                                                      Resources.RUBY: 0,
                                                                                      Resources.SAPPHIRE: 0})))
    # SAPPHIRE                                                                                                                                                                                                                   
    cards.append(DevelopmentCard(level=2, gift=Resources.SAPPHIRE, score=1, cost=Counter({Resources.DIAMOND: 0,
                                                                                          Resources.EMERALD: 2,
                                                                                          Resources.ONYX: 0,
                                                                                          Resources.RUBY: 3,
                                                                                          Resources.SAPPHIRE: 2}))) 
    cards.append(DevelopmentCard(level=2, gift=Resources.SAPPHIRE, score=1, cost=Counter({Resources.DIAMOND: 0,
                                                                                          Resources.EMERALD: 3,
                                                                                          Resources.ONYX: 3,
                                                                                          Resources.RUBY: 0,
                                                                                          Resources.SAPPHIRE: 2})))  
    cards.append(DevelopmentCard(level=2, gift=Resources.SAPPHIRE, score=2, cost=Counter({Resources.DIAMOND: 5,
                                                                                          Resources.EMERALD: 0,
                                                                                          Resources.ONYX: 0,
                                                                                          Resources.RUBY: 0,
                                                                                          Resources.SAPPHIRE: 3})))     
    cards.append(DevelopmentCard(level=2, gift=Resources.SAPPHIRE, score=2, cost=Counter({Resources.DIAMOND: 0,
                                                                                          Resources.EMERALD: 0,
                                                                                          Resources.ONYX: 0,
                                                                                          Resources.RUBY: 0,
                                                                                          Resources.SAPPHIRE: 5})))
    cards.append(DevelopmentCard(level=2, gift=Resources.SAPPHIRE, score=2, cost=Counter({Resources.DIAMOND: 2,
                                                                                          Resources.EMERALD: 0,
                                                                                          Resources.ONYX: 4,
                                                                                          Resources.RUBY: 1,
                                                                                          Resources.SAPPHIRE: 0})))
    cards.append(DevelopmentCard(level=2, gift=Resources.SAPPHIRE, score=3, cost=Counter({Resources.DIAMOND: 0,
                                                                                          Resources.EMERALD: 0,
                                                                                          Resources.ONYX: 0,
                                                                                          Resources.RUBY: 0,
                                                                                          Resources.SAPPHIRE: 6})))  
    # EMERALD                                                                                                                                                                                                                                     
    cards.append(DevelopmentCard(level=2, gift=Resources.EMERALD, score=1, cost=Counter({Resources.DIAMOND: 3,
                                                                                         Resources.EMERALD: 2,
                                                                                         Resources.ONYX: 0,
                                                                                         Resources.RUBY: 3,
                                                                                         Resources.SAPPHIRE: 0}))) 
    cards.append(DevelopmentCard(level=2, gift=Resources.EMERALD, score=1, cost=Counter({Resources.DIAMOND: 2,
                                                                                         Resources.EMERALD: 0,
                                                                                         Resources.ONYX: 2,
                                                                                         Resources.RUBY: 0,
                                                                                         Resources.SAPPHIRE: 3})))  
    cards.append(DevelopmentCard(level=2, gift=Resources.EMERALD, score=2, cost=Counter({Resources.DIAMOND: 4,
                                                                                         Resources.EMERALD: 0,
                                                                                         Resources.ONYX: 1,
                                                                                         Resources.RUBY: 0,
                                                                                         Resources.SAPPHIRE: 2})))     
    cards.append(DevelopmentCard(level=2, gift=Resources.EMERALD, score=2, cost=Counter({Resources.DIAMOND: 0,
                                                                                         Resources.EMERALD: 5,
                                                                                         Resources.ONYX: 0,
                                                                                         Resources.RUBY: 0,
                                                                                         Resources.SAPPHIRE: 0})))
    cards.append(DevelopmentCard(level=2, gift=Resources.EMERALD, score=2, cost=Counter({Resources.DIAMOND: 0,
                                                                                         Resources.EMERALD: 3,
                                                                                         Resources.ONYX: 0,
                                                                                         Resources.RUBY: 0,
                                                                                         Resources.SAPPHIRE: 5})))
    cards.append(DevelopmentCard(level=2, gift=Resources.EMERALD, score=3, cost=Counter({Resources.DIAMOND: 0,
                                                                                         Resources.EMERALD: 6,
                                                                                         Resources.ONYX: 0,
                                                                                         Resources.RUBY: 0,
                                                                                         Resources.SAPPHIRE: 0})))
    # RUBY                                                                                                                                                                                                                         
    cards.append(DevelopmentCard(level=2, gift=Resources.RUBY, score=1, cost=Counter({Resources.DIAMOND: 0,
                                                                                      Resources.EMERALD: 0,
                                                                                      Resources.ONYX: 3,
                                                                                      Resources.RUBY: 2,
                                                                                      Resources.SAPPHIRE: 3}))) 
    cards.append(DevelopmentCard(level=2, gift=Resources.RUBY, score=1, cost=Counter({Resources.DIAMOND: 2,
                                                                                      Resources.EMERALD: 0,
                                                                                      Resources.ONYX: 3,
                                                                                      Resources.RUBY: 2,
                                                                                      Resources.SAPPHIRE: 0})))  
    cards.append(DevelopmentCard(level=2, gift=Resources.RUBY, score=2, cost=Counter({Resources.DIAMOND: 1,
                                                                                      Resources.EMERALD: 2,
                                                                                      Resources.ONYX: 0,
                                                                                      Resources.RUBY: 0,
                                                                                      Resources.SAPPHIRE: 4})))     
    cards.append(DevelopmentCard(level=2, gift=Resources.RUBY, score=2, cost=Counter({Resources.DIAMOND: 3,
                                                                                      Resources.EMERALD: 0,
                                                                                      Resources.ONYX: 5,
                                                                                      Resources.RUBY: 0,
                                                                                      Resources.SAPPHIRE: 0})))
    cards.append(DevelopmentCard(level=2, gift=Resources.RUBY, score=2, cost=Counter({Resources.DIAMOND: 0,
                                                                                      Resources.EMERALD: 0,
                                                                                      Resources.ONYX: 5,
                                                                                      Resources.RUBY: 0,
                                                                                      Resources.SAPPHIRE: 0})))
    cards.append(DevelopmentCard(level=2, gift=Resources.RUBY, score=3, cost=Counter({Resources.DIAMOND: 0,
                                                                                      Resources.EMERALD: 0,
                                                                                      Resources.ONYX: 0,
                                                                                      Resources.RUBY: 6,
                                                                                      Resources.SAPPHIRE: 0})))
    # DIAMOND
    cards.append(DevelopmentCard(level=2, gift=Resources.DIAMOND, score=1, cost=Counter({Resources.DIAMOND: 0,
                                                                                         Resources.EMERALD: 3,
                                                                                         Resources.ONYX: 2,
                                                                                         Resources.RUBY: 2,
                                                                                         Resources.SAPPHIRE: 0}))) 
    cards.append(DevelopmentCard(level=2, gift=Resources.DIAMOND, score=1, cost=Counter({Resources.DIAMOND: 2,
                                                                                         Resources.EMERALD: 0,
                                                                                         Resources.ONYX: 0,
                                                                                         Resources.RUBY: 3,
                                                                                         Resources.SAPPHIRE: 3})))  
    cards.append(DevelopmentCard(level=2, gift=Resources.DIAMOND, score=2, cost=Counter({Resources.DIAMOND: 0,
                                                                                         Resources.EMERALD: 1,
                                                                                         Resources.ONYX: 2,
                                                                                         Resources.RUBY: 4,
                                                                                         Resources.SAPPHIRE: 0})))     
    cards.append(DevelopmentCard(level=2, gift=Resources.DIAMOND, score=2, cost=Counter({Resources.DIAMOND: 0,
                                                                                         Resources.EMERALD: 0,
                                                                                         Resources.ONYX: 0,
                                                                                         Resources.RUBY: 5,
                                                                                         Resources.SAPPHIRE: 0})))
    cards.append(DevelopmentCard(level=2, gift=Resources.DIAMOND, score=2, cost=Counter({Resources.DIAMOND: 0,
                                                                                         Resources.EMERALD: 0,
                                                                                         Resources.ONYX: 3,
                                                                                         Resources.RUBY: 5,
                                                                                         Resources.SAPPHIRE: 0})))
    cards.append(DevelopmentCard(level=2, gift=Resources.DIAMOND, score=3, cost=Counter({Resources.DIAMOND: 6,
                                                                                         Resources.EMERALD: 0,
                                                                                         Resources.ONYX: 0,
                                                                                         Resources.RUBY: 0,
                                                                                         Resources.SAPPHIRE: 0})))     
    return cards                


def get_all_third_level_development_cards() -> List[DevelopmentCard]:
    cards: List[DevelopmentCard] = []
    # ONYX                                 
    cards.append(DevelopmentCard(level=3, gift=Resources.ONYX, score=3, cost=Counter({Resources.DIAMOND: 3,
                                                                                      Resources.EMERALD: 5,
                                                                                      Resources.ONYX: 0,
                                                                                      Resources.RUBY: 3,
                                                                                      Resources.SAPPHIRE: 3})))
    cards.append(DevelopmentCard(level=3, gift=Resources.ONYX, score=4, cost=Counter({Resources.DIAMOND: 0,
                                                                                      Resources.EMERALD: 0,
                                                                                      Resources.ONYX: 0,
                                                                                      Resources.RUBY: 7,
                                                                                      Resources.SAPPHIRE: 0})))
    cards.append(DevelopmentCard(level=3, gift=Resources.ONYX, score=4, cost=Counter({Resources.DIAMOND: 0,
                                                                                      Resources.EMERALD: 3,
                                                                                      Resources.ONYX: 3,
                                                                                      Resources.RUBY: 6,
                                                                                      Resources.SAPPHIRE: 0})))        
    cards.append(DevelopmentCard(level=3, gift=Resources.ONYX, score=5, cost=Counter({Resources.DIAMOND: 0,
                                                                                      Resources.EMERALD: 0,
                                                                                      Resources.ONYX: 3,
                                                                                      Resources.RUBY: 7,
                                                                                      Resources.SAPPHIRE: 0})))
    # SAPPHIRE                                                                                                                                                                                                                   
    cards.append(DevelopmentCard(level=3, gift=Resources.SAPPHIRE, score=3, cost=Counter({Resources.DIAMOND: 3,
                                                                                          Resources.EMERALD: 3,
                                                                                          Resources.ONYX: 5,
                                                                                          Resources.RUBY: 3,
                                                                                          Resources.SAPPHIRE: 0})))     
    cards.append(DevelopmentCard(level=3, gift=Resources.SAPPHIRE, score=4, cost=Counter({Resources.DIAMOND: 7,
                                                                                          Resources.EMERALD: 0,
                                                                                          Resources.ONYX: 0,
                                                                                          Resources.RUBY: 0,
                                                                                          Resources.SAPPHIRE: 0})))
    cards.append(DevelopmentCard(level=3, gift=Resources.SAPPHIRE, score=4, cost=Counter({Resources.DIAMOND: 6,
                                                                                          Resources.EMERALD: 0,
                                                                                          Resources.ONYX: 3,
                                                                                          Resources.RUBY: 0,
                                                                                          Resources.SAPPHIRE: 3})))
    cards.append(DevelopmentCard(level=3, gift=Resources.SAPPHIRE, score=5, cost=Counter({Resources.DIAMOND: 7,
                                                                                          Resources.EMERALD: 0,
                                                                                          Resources.ONYX: 0,
                                                                                          Resources.RUBY: 0,
                                                                                          Resources.SAPPHIRE: 3})))  
    # EMERALD                                                                                                                                                                                                                                      
    cards.append(DevelopmentCard(level=3, gift=Resources.EMERALD, score=3, cost=Counter({Resources.DIAMOND: 5,
                                                                                         Resources.EMERALD: 0,
                                                                                         Resources.ONYX: 3,
                                                                                         Resources.RUBY: 3,
                                                                                         Resources.SAPPHIRE: 3})))     
    cards.append(DevelopmentCard(level=3, gift=Resources.EMERALD, score=4, cost=Counter({Resources.DIAMOND: 3,
                                                                                         Resources.EMERALD: 3,
                                                                                         Resources.ONYX: 0,
                                                                                         Resources.RUBY: 0,
                                                                                         Resources.SAPPHIRE: 6})))
    cards.append(DevelopmentCard(level=3, gift=Resources.EMERALD, score=4, cost=Counter({Resources.DIAMOND: 0,
                                                                                         Resources.EMERALD: 0,
                                                                                         Resources.ONYX: 0,
                                                                                         Resources.RUBY: 0,
                                                                                         Resources.SAPPHIRE: 7})))
    cards.append(DevelopmentCard(level=3, gift=Resources.EMERALD, score=5, cost=Counter({Resources.DIAMOND: 0,
                                                                                         Resources.EMERALD: 3,
                                                                                         Resources.ONYX: 0,
                                                                                         Resources.RUBY: 0,
                                                                                         Resources.SAPPHIRE: 7})))
    # RUBY                                                                                                                                                                                                                         
    cards.append(DevelopmentCard(level=3, gift=Resources.RUBY, score=3, cost=Counter({Resources.DIAMOND: 3,
                                                                                      Resources.EMERALD: 3,
                                                                                      Resources.ONYX: 3,
                                                                                      Resources.RUBY: 0,
                                                                                      Resources.SAPPHIRE: 5})))     
    cards.append(DevelopmentCard(level=3, gift=Resources.RUBY, score=4, cost=Counter({Resources.DIAMOND: 0,
                                                                                      Resources.EMERALD: 7,
                                                                                      Resources.ONYX: 0,
                                                                                      Resources.RUBY: 0,
                                                                                      Resources.SAPPHIRE: 0})))
    cards.append(DevelopmentCard(level=3, gift=Resources.RUBY, score=4, cost=Counter({Resources.DIAMOND: 0,
                                                                                      Resources.EMERALD: 6,
                                                                                      Resources.ONYX: 0,
                                                                                      Resources.RUBY: 3,
                                                                                      Resources.SAPPHIRE: 3})))
    cards.append(DevelopmentCard(level=3, gift=Resources.RUBY, score=5, cost=Counter({Resources.DIAMOND: 0,
                                                                                      Resources.EMERALD: 7,
                                                                                      Resources.ONYX: 0,
                                                                                      Resources.RUBY: 3,
                                                                                      Resources.SAPPHIRE: 0})))
    # DIAMOND
    cards.append(DevelopmentCard(level=3, gift=Resources.DIAMOND, score=3, cost=Counter({Resources.DIAMOND: 0,
                                                                                         Resources.EMERALD: 3,
                                                                                         Resources.ONYX: 3,
                                                                                         Resources.RUBY: 5,
                                                                                         Resources.SAPPHIRE: 3})))     
    cards.append(DevelopmentCard(level=3, gift=Resources.DIAMOND, score=4, cost=Counter({Resources.DIAMOND: 0,
                                                                                         Resources.EMERALD: 0,
                                                                                         Resources.ONYX: 7,
                                                                                         Resources.RUBY: 0,
                                                                                         Resources.SAPPHIRE: 0})))
    cards.append(DevelopmentCard(level=3, gift=Resources.DIAMOND, score=4, cost=Counter({Resources.DIAMOND: 3,
                                                                                         Resources.EMERALD: 0,
                                                                                         Resources.ONYX: 6,
                                                                                         Resources.RUBY: 3,
                                                                                         Resources.SAPPHIRE: 0})))
    cards.append(DevelopmentCard(level=3, gift=Resources.DIAMOND, score=5, cost=Counter({Resources.DIAMOND: 3,
                                                                                         Resources.EMERALD: 0,
                                                                                         Resources.ONYX: 7,
                                                                                         Resources.RUBY: 0,
                                                                                         Resources.SAPPHIRE: 0})))     
    return cards                                                                                                


def get_all_noble_tiles():
    noble_tiles: List[NobleTile] = []
    noble_tiles.append(NobleTile(cost=Counter({Resources.DIAMOND: 0,
                                               Resources.EMERALD: 4,
                                               Resources.ONYX: 0,
                                               Resources.RUBY: 4,
                                               Resources.SAPPHIRE: 0})))
    noble_tiles.append(NobleTile(cost=Counter({Resources.DIAMOND: 3,
                                               Resources.EMERALD: 0,
                                               Resources.ONYX: 3,
                                               Resources.RUBY: 3,
                                               Resources.SAPPHIRE: 0})))
    noble_tiles.append(NobleTile(cost=Counter({Resources.DIAMOND: 4,
                                               Resources.EMERALD: 0,
                                               Resources.ONYX: 0,
                                               Resources.RUBY: 0,
                                               Resources.SAPPHIRE: 4})))
    noble_tiles.append(NobleTile(cost=Counter({Resources.DIAMOND: 4,
                                               Resources.EMERALD: 0,
                                               Resources.ONYX: 4,
                                               Resources.RUBY: 0,
                                               Resources.SAPPHIRE: 0})))
    noble_tiles.append(NobleTile(cost=Counter({Resources.DIAMOND: 0,
                                               Resources.EMERALD: 4,
                                               Resources.ONYX: 0,
                                               Resources.RUBY: 0,
                                               Resources.SAPPHIRE: 4})))
    noble_tiles.append(NobleTile(cost=Counter({Resources.DIAMOND: 0,
                                               Resources.EMERALD: 3,
                                               Resources.ONYX: 0,
                                               Resources.RUBY: 3,
                                               Resources.SAPPHIRE: 3})))
    noble_tiles.append(NobleTile(cost=Counter({Resources.DIAMOND: 3,
                                               Resources.EMERALD: 3,
                                               Resources.ONYX: 0,
                                               Resources.RUBY: 0,
                                               Resources.SAPPHIRE: 3})))
    noble_tiles.append(NobleTile(cost=Counter({Resources.DIAMOND: 0,
                                               Resources.EMERALD: 0,
                                               Resources.ONYX: 4,
                                               Resources.RUBY: 4,
                                               Resources.SAPPHIRE: 0})))
    noble_tiles.append(NobleTile(cost=Counter({Resources.DIAMOND: 3,
                                               Resources.EMERALD: 0,
                                               Resources.ONYX: 3,
                                               Resources.RUBY: 0,
                                               Resources.SAPPHIRE: 3})))
    noble_tiles.append(NobleTile(cost=Counter({Resources.DIAMOND: 0,
                                               Resources.EMERALD: 3,
                                               Resources.ONYX: 3,
                                               Resources.RUBY: 3,
                                               Resources.SAPPHIRE: 0})))
    return noble_tiles
