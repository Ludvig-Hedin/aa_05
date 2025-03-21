import os
import sys
import importlib.util
from typing import Dict, List, Any, Optional

# Add component paths to system path
COMPONENTS_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "components")
COMPONENT_MODULES = {
    "autogpt": os.path.join(COMPONENTS_PATH, "autogpt"),
    "langchain": os.path.join(COMPONENTS_PATH, "langchain"),
    "llama_cpp": os.path.join(COMPONENTS_PATH, "llama-cpp-python"),
    "browser_use": os.path.join(COMPONENTS_PATH, "browser-use"),
    "browser_web_ui": os.path.join(COMPONENTS_PATH, "browser-web-ui"),
    "researcher": os.path.join(COMPONENTS_PATH, "gpt-researcher"),
    "jobs_applier": os.path.join(COMPONENTS_PATH, "jobs-applier"),
    "openmanus": os.path.join(COMPONENTS_PATH, "openmanus"),
    "agent_zero": os.path.join(COMPONENTS_PATH, "agent-zero"),
    "csm": os.path.join(COMPONENTS_PATH, "csm"),
    "deepseek": os.path.join(COMPONENTS_PATH, "deepseek-r1"),
    "mem0": os.path.join(COMPONENTS_PATH, "mem0"),
    "n8n": os.path.join(COMPONENTS_PATH, "n8n"),
    "supabase": os.path.join(COMPONENTS_PATH, "supabase"),
    "wan_video": os.path.join(COMPONENTS_PATH, "wan-video"),
}

# Add paths to Python path
for module_path in COMPONENT_MODULES.values():
    if module_path not in sys.path and os.path.exists(module_path):
        sys.path.append(module_path)

class AAIntegration:
    """Main integration class for AA-05 platform"""
    
    def __init__(self, config_path: Optional[str] = None):
        self.components = {}
        self.config = self._load_config(config_path)
        self._initialize_components()
    
    def _load_config(self, config_path: Optional[str]) -> Dict[str, Any]:
        """Load configuration from file or use defaults"""
        if config_path and os.path.exists(config_path):
            import json
            with open(config_path, 'r') as f:
                return json.load(f)
        return {
            "enabled_components": ["autogpt", "langchain", "llama_cpp", "browser_use", "mem0"],
            "api_keys": {},
            "model_paths": {},
            "default_agent": "autogpt"
        }
    
    def _initialize_components(self):
        """Initialize all enabled components"""
        for component_name in self.config["enabled_components"]:
            if component_name in COMPONENT_MODULES:
                self._load_component(component_name)
    
    def _load_component(self, component_name: str):
        """Load a specific component by name"""
        try:
            module_path = COMPONENT_MODULES.get(component_name)
            if not module_path or not os.path.exists(module_path):
                print(f"Component path not found: {component_name}")
                return False
                
            # Determine the main module to import
            if component_name == "autogpt":
                self.components[component_name] = self._import_autogpt()
            elif component_name == "langchain":
                self.components[component_name] = self._import_langchain()
            elif component_name == "llama_cpp":
                self.components[component_name] = self._import_llama_cpp()
            elif component_name == "browser_use":
                self.components[component_name] = self._import_browser_use()
            elif component_name == "mem0":
                self.components[component_name] = self._import_mem0()
            elif component_name == "researcher":
                self.components[component_name] = self._import_researcher()
            elif component_name == "n8n":
                self.components[component_name] = self._import_n8n()
            elif component_name == "supabase":
                self.components[component_name] = self._import_supabase()
            elif component_name == "wan_video":
                self.components[component_name] = self._import_wan_video()
            # Add other components here...
            
            return True
        except Exception as e:
            print(f"Error loading component {component_name}: {str(e)}")
            return False
    
    def _import_autogpt(self):
        """Import AutoGPT components"""
        # Implementation for AutoGPT integration
        return {"status": "loaded"}
    
    def _import_langchain(self):
        """Import LangChain components"""
        # Implementation for LangChain integration
        return {"status": "loaded"}
    
    def _import_llama_cpp(self):
        """Import llama-cpp-python components"""
        # Implementation for llama-cpp-python integration
        return {"status": "loaded"}
    
    def _import_browser_use(self):
        """Import browser-use components"""
        # Implementation for browser-use integration
        return {"status": "loaded"}
    
    def _import_mem0(self):
        """Import mem0 components for memory management"""
        # Implementation for mem0 integration
        return {"status": "loaded"}
    
    def _import_researcher(self):
        """Import researcher components"""
        # Implementation for gpt-researcher integration
        return {"status": "loaded"}
    
    def _import_n8n(self):
        """Import n8n workflow automation components"""
        # Implementation for n8n integration
        return {"status": "loaded"}
    
    def _import_supabase(self):
        """Import Supabase database components"""
        # Implementation for Supabase integration
        return {"status": "loaded"}
    
    def _import_wan_video(self):
        """Import video processing components"""
        # Implementation for Wan Video integration
        return {"status": "loaded"}
    
    # Add more component import methods as needed...
    
    def get_agent(self, agent_type: str = None):
        """Get an agent of the specified type or default"""
        agent_type = agent_type or self.config["default_agent"]
        
        if agent_type == "autogpt" and "autogpt" in self.components:
            return self._create_autogpt_agent()
        elif agent_type == "langchain" and "langchain" in self.components:
            return self._create_langchain_agent()
        elif agent_type == "researcher" and "researcher" in self.components:
            return self._create_researcher_agent()
        # Add other agent types...
        
        raise ValueError(f"Agent type not supported or not loaded: {agent_type}")
    
    def _create_autogpt_agent(self):
        """Create an AutoGPT agent"""
        # Implementation for creating AutoGPT agent
        return {"agent_type": "autogpt"}
    
    def _create_langchain_agent(self):
        """Create a LangChain agent"""
        # Implementation for creating LangChain agent
        return {"agent_type": "langchain"}
    
    def _create_researcher_agent(self):
        """Create a Researcher agent"""
        # Implementation for creating Researcher agent
        return {"agent_type": "researcher"}
    
    # Add more agent creation methods as needed...