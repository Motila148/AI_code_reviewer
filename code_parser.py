import ast
import time
from typing import Any, Dict, List, Optional

class CodeParser:
    """
    Responsibilities:
    - Validate input code
    - Perform safe AST parsing
    - Capture structured syntax errors
    - Provide AST to downstream analyzers
    """
    def __init__(self, filename: Optional[str] = None):
        self.filenmae = filename
        self.source_code: Optional[str] = None
        self.ast_trees: Optional[ast.AST] = None
        self.syntax_errors: List[Dict[str, Any]] = []
        self.parse_success: bool = False
        self.parsing_time: float = 0.0

    
    def parse(self, code: str) -> Dict[str, Any]:
        """
        Main enrty point for parsing.
        Returns structured ParseResult.
        """
        self._reset_state()
        self.source_code = code

        start_time = time.time()


        # Validate input
        if not self._validate_input(code):
            self.parsing_time = time.time() - start_time
            return self._build_result()
        
        # Safe parse attempt

        self._safe_parse(code)


        self.parsing_time = time.time() - start_time
        return self._build_result()
    
        
    def has_syntax_errors(self) -> bool:
        """
        Quick check for syntax errors.
        """
        return len(self.syntax_errors) > 0
    

    def get_ast(self) -> Optional[ast.AST]:
        """ Return AST if parsing succeeded."""
        return self.ast_trees if self.parse_success else None
    
    def get_errors(self) -> List[Dict[str, Any]]:
        """ 
        Return Structured syntax errors.
        """
        return self.syntax_errors
    
    # Internal Helper

    def _reset_state(self) -> None:
        """
        Reset parser before before each run.
        """
        self.ast_trees = None
        self.syntax_errors = []
        self.parse_success = False
        self.parsing_time = 0.0

    def _validate_input(self, code: Any) -> bool:
        """ 
        Basic input validation 
        """
        if not isinstance(code, str):
            self.syntax_errors.append({
                "type": "InputError",
                "line": None,
                "column": None,
                "message": "Source code must be a string",
                "severity": "error",
                "stage": "syntax"
            })
            return False
        if code.strip() == "":
            self.syntax_errors.append({
                "type": "InputError",
                "line": None,
                "column": None,
                "message": "Source code must be a string",
                "severity": "error",
                "stage": "syntax"
            })
            return False
        
        return True
    
    def _safe_parse(self, code: str) -> None:
        """
        Attempt safe parsing.
        """
        try:
            self.ast_trees = ast.parse(code)
            self.parse_success = True

        except SyntaxError as e:
            self.parse_success = False
            self.syntax_errors.append(self._format_syntax_errors(e))

        except Exception as e:
            # Catche unexpected parser failures
            self.parse_success = False
            self.syntax_errors.append({

                "type": "ParseError",
                "line": None,
                "column": None,
                "message": str(e),
                "severity": "error",
                "stage": "syntax"
            })


    def _format_syntax_errors(self, exc: SyntaxError) -> Dict[str, Any]:
        """  
        Convert syntax error in structured format.
        """
        return {
            "type": "ParseError",
            "line": exc.lineno,
            "column": exc.offset,
            "message": exc.msg,
            "severity": "error",
            "stage": "syntax"
            
        }
    
    def _build_result(self) -> Dict[str, Any]:
        """  
        Build structured parse result.
        """
        return {
            "success": self.parse_success,
            "ast_tree": self.ast_trees,
            "syntax_errors": self.syntax_errors,
            "parsing_time": self.parsing_time,
        }
    

parser = CodeParser()
code = """ 
def calculate_area(radius):
    # Error 1: Missing colon in function definition above
    
    if radius > 0:
        # Error 2: Missing colon in if-statement
        import math
        return math.pi * (radius ** 2)
    else:
        return "Invalid radius"

# Error 3: Misplaced indentation and missing closing quote
print(calculate_area(5))
"""
while code
print(parser.parse(code))