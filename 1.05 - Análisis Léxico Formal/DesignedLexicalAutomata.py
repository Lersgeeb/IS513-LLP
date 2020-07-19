from AlphabetSets import AlphabetSets

class DesignedLexicalAutomata:
    
    STATES = [
            'start',
            'ident',
            'int',
            'waitFloat',
            'float',
            'operator',
            'conditionAssign',
            'classToken',
            'lookup',
            'waitString1',
            'waitString2',
            'string',
            'error',
        ]

    TRANSITIONS = {
        'start':{
            AlphabetSets.ALPHA:'ident',
            AlphabetSets.DIGIT:'int',
            AlphabetSets.ASCII:'error', 
            '/*-+^%':'operator',
            '=><!':'conditionAssign',
            ':':'classToken',
            ';{(})#,.':'lookup',
            '"':'waitString1',
            "'":'waitString2',
            ' ':'start',
            '\t':'start',
            '\n':'start',
        },
        
        'ident':{
            AlphabetSets.ALPHA:'ident',
            AlphabetSets.DIGIT:'ident',
            AlphabetSets.ASCII:'error',
            '_':'ident',
            '/*-+^%':'operator',
            '=><!':'conditionAssign',
            ':':'classToken',
            ';{(}),.':'lookup',
            ' ':'start',
            '\t':'start',
            '\n':'start',
        },
        
        'int':{
            AlphabetSets.DIGIT:'int',
            AlphabetSets.ASCII:'error',
            '.':'waitFloat',
            '/*-+^%':'operator',
            '=><!':'conditionAssign',
            ';{(})#,':'lookup',
            ' ':'start',
            '\t':'start',
            '\n':'start',
        },
        
        'waitFloat':{AlphabetSets.DIGIT:'float', AlphabetSets.ASCII:'error'},
        'float':{
            AlphabetSets.DIGIT:'float',
            AlphabetSets.ASCII:'error', 
            '/*-+^%':'operator',
            '=><!':'conditionAssign',
            ';{(})#,.':'lookup',
            ' ':'start',
            '\t':'start',
            '\n':'start',
        },
        
        'operator':{
            AlphabetSets.ALPHA:'ident',
            AlphabetSets.DIGIT:'int',
            AlphabetSets.ASCII:'error',
            '/*-+^%':'operator',
            '=><!':'conditionAssign',
            ':':'classToken',
            ';{(})#,.':'lookup',
            ' ':'start',
            '\t':'start',
            '\n':'start',
        },
        
        'conditionAssign':{
            AlphabetSets.ALPHA:'ident',
            AlphabetSets.DIGIT:'int',
            AlphabetSets.ASCII:'error',
            '=<>':'conditionAssign', 
            ':':'classToken',
            ';{(})#,.':'lookup',
            ' ':'start',
            '\t':'start',
            '\n':'start',
        },

        'classToken':{
            AlphabetSets.ALPHA:'ident',
            AlphabetSets.DIGIT:'int',
            AlphabetSets.ASCII:'error',
            ":":"classToken",
            '/*-+^%':'operator',
            '=><!':'conditionAssign',
            ';{(})#,.':'lookup',
            ' ':'start',
            '\t':'start',
            '\n':'start',
        },

        'lookup':{
            AlphabetSets.ALPHA:'ident',
            AlphabetSets.DIGIT:'int',
            AlphabetSets.ASCII:'error',
            ":":"classToken",
            '/*-+^%':'operator',
            '=><!':'conditionAssign',
            ';{(})#,.':'lookup',
            ' ':'start',
            '\t':'start',
            '\n':'start',
        },

        'waitString1':{
            '"':'string',
            AlphabetSets.ASCII:'waitString1'
        },
        'waitString2':{
            "'":'string',
            AlphabetSets.ASCII:'waitString2'
        },            
        'string':{
            '"':'waitString1',
            "'":'waitString2',
            AlphabetSets.ALPHA:'ident',
            AlphabetSets.DIGIT:'int',
            AlphabetSets.ASCII:'error',
            '/*-+^%':'operator',
            '=><!':'conditionAssign',
            ';{(})#,.':'lookup',
            ":":"classToken",
            ' ':'start',
            '\t':'start',
            '\n':'start',
        },
        'error':{
            AlphabetSets.ASCII:'error',
        }

    }
    #FINALSTATE = {'q3':'COMMENT'}

    