{
    "variables": {
      "ndi_dir": "<(module_root_dir)/ndi"
    },
    "targets": [ {
        "target_name": "grandiose",
        "sources": [
            "src/grandiose_util.cc",
            "src/grandiose_find.cc",
            "src/grandiose_send.cc",
            "src/grandiose_receive.cc",
            "src/grandiose_routing.cc",
            "src/grandiose.cc"
        ],
        "include_dirs": [ "ndi/include" ],
        "conditions":[
            [ "OS == 'win' and target_arch == 'ia32'", {
                "copies": [ {
                    "destination":  "build/Release",
                    "files":        [ "<(ndi_dir)/lib/win-x86/Processing.NDI.Lib.x86.dll" ]
                } ],
                "link_settings": {
                    "libraries":    [ "Processing.NDI.Lib.x86.lib" ],
                    "library_dirs": [ "<(ndi_dir)/lib/win-x86" ]
                }
            } ],
            [ "OS == 'win' and target_arch == 'x64'", {
                "copies": [ {
                    "destination":  "build/Release",
                    "files":        [ "<(ndi_dir)/lib/win-x64/Processing.NDI.Lib.x64.dll" ]
                } ],
                "link_settings": {
                    "libraries":    [ "Processing.NDI.Lib.x64.lib" ],
                    "library_dirs": [ "<(ndi_dir)/lib/win-x64" ]
                }
            } ],
            [ "OS == 'linux' and target_arch == 'ia32'", {
                "copies": [ {
                    "destination":  "build/Release",
                    "files":        [ "<(ndi_dir)/lib/lnx-x86/libndi.so",
                                      "<(ndi_dir)/lib/lnx-x86/libndi.so.5",
                                      "<(ndi_dir)/lib/lnx-x86/libndi.so.5.1.1" ]
                } ],
                "link_settings": {
                    "libraries":    [ "-Wl,-rpath,'$$ORIGIN'", "-lndi" ],
                    "library_dirs": [ "<(ndi_dir)/lib/lnx-x86" ]
                }
            } ],
            [ "OS == 'linux' and target_arch == 'x64'", {
                "copies": [ {
                    "destination":  "build/Release",
                    "files":        [ "<(ndi_dir)/lib/lnx-x64/libndi.so",
                                      "<(ndi_dir)/lib/lnx-x64/libndi.so.5",
                                      "<(ndi_dir)/lib/lnx-x64/libndi.so.5.1.1" ]
                } ],
                "link_settings": {
                    "libraries":    [ "-Wl,-rpath,'$$ORIGIN'", "-lndi" ],
                    "library_dirs": [ "<(ndi_dir)/lib/lnx-x64" ]
                }
            } ],
            [ "OS == 'mac'", {
                "copies": [ {
                    "destination":  "build/Release",
                    "files":        [ "<(ndi_dir)/lib/mac/libndi.dylib" ]
                } ],
                "link_settings": {
                    "libraries":    [ "-Wl,-rpath,@loader_path", "-lndi" ],
                    "library_dirs": [ "<(ndi_dir)/lib/mac" ]
                }
            } ]
        ]
    } ]
}
