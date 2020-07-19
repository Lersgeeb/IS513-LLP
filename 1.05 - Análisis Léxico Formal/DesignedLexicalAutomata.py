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
            '/*-+^%':'operator',
            '=><!':'conditionAssign',
            ':':'classToken',
            ';{(}),.':'lookup',
            ' ':'start',
            '\t':'start',
            '\n':'start',
        },
        
        'int':{
            AlphabetSets.ALPHA:'error',
            AlphabetSets.DIGIT:'int',
            AlphabetSets.ASCII:'start',
            '.':'waitFloat',
            '/*-+^%':'operator',
            '=><!':'conditionAssign',
            ':':'classToken',
            ';{(})#,':'lookup',
        },
        
        'waitFloat':{AlphabetSets.DIGIT:'float', AlphabetSets.ASCII:'error'},
        'float':{
            AlphabetSets.DIGIT:'float',
            AlphabetSets.ASCII:'start', 
            '/*-+^%':'operator',
            '=><!':'conditionAssign',
            ':':'classToken',
            ';{(})#,.':'lookup',
        },
        
        'operator':{
            AlphabetSets.ALPHA:'ident',
            AlphabetSets.DIGIT:'int',
            AlphabetSets.ASCII:'start',
            '/*-+^%':'operator',
            '=><!':'conditionAssign',
            ':':'classToken',
            ';{(})#,.':'lookup',
        },
        
        'conditionAssign':{
            AlphabetSets.ALPHA:'ident',
            AlphabetSets.DIGIT:'int',
            AlphabetSets.ASCII:'start',
            '=<>':'conditionAssign', 
            ':':'classToken',
            ';{(})#,.':'lookup',
        },

        'classToken':{
            AlphabetSets.ALPHA:'ident',
            AlphabetSets.DIGIT:'int',
            AlphabetSets.ASCII:'start',
            ":":"classToken",
            '/*-+^%':'operator',
            '=><!':'conditionAssign',
            ';{(})#,.':'lookup',
        },

        'lookup':{
            AlphabetSets.ALPHA:'ident',
            AlphabetSets.DIGIT:'int',
            AlphabetSets.ASCII:'start',
            ":":"classToken",
            '/*-+^%':'operator',
            '=><!':'conditionAssign',
            ';{(})#,.':'lookup',
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
            AlphabetSets.ASCII:'start',
            '/*-+^%':'operator',
            '=><!':'conditionAssign',
            ';{(})#,.':'lookup',
            ":":"classToken",
        },

    }
    #FINALSTATE = {'q3':'COMMENT'}

    