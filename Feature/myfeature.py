"""
Feature module for myfeature functionality.
"""


class MyFeature:
    """A simple feature class."""
    
    def __init__(self, name: str):
        """Initialize the feature with a name.
        
        Args:
            name: The name of the feature.
        """
        self.name = name
    
    def execute(self) -> str:
        """Execute the feature.
        
        Returns:
            A message indicating the feature executed successfully.
        """
        return f"Feature '{self.name}' executed successfully"
    
    def get_info(self) -> dict:
        """Get feature information.
        
        Returns:
            A dictionary with feature details.
        """
        return {
            "name": self.name,
            "status": "active"
        }


if __name__ == "__main__":
    feature = MyFeature("myfeature")
    print(feature.execute())
    print(feature.get_info())
    print("Welcome to DevAsc")
    