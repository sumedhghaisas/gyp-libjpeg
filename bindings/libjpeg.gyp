{
  'variables': { 'target_arch%': 'ia32' },

  'target_defaults': {
    'default_configuration': 'Debug',
    'configurations': {
      'Debug': {
        'defines': [ 'DEBUG', '_DEBUG' ],
        'msvs_settings': {
          'VCCLCompilerTool': {
            'RuntimeLibrary': 1, # static debug
          },
        },
      },
      'Release': {
        'defines': [ 'NDEBUG' ],
        'msvs_settings': {
          'VCCLCompilerTool': {
            'RuntimeLibrary': 0, # static release
          },
        },
      }
    },
    'msvs_settings': {
      'VCLinkerTool': {
        'GenerateDebugInformation': 'true',
      },
    },
    'include_dirs': [
       # platform and arch-specific headers
       '../config/<(OS)/<(target_arch)'
     ],
  },

  "targets": [
        {
            "target_name": "libjpeg",
	    'product_prefix': 'lib',
            "type": "static_library",
            "include_dirs": [
                "../libjpeg"
            ],
            "sources": [
                "../libjpeg/ansi2knr.c",
                "../libjpeg/cdjpeg.c",
                "../libjpeg/cjpeg.c",
                "../libjpeg/ckconfig.c",
                "../libjpeg/djpeg.c",
                "../libjpeg/jaricom.c",
		"../libjpeg/jcapimin.c",
                "../libjpeg/jcapistd.c",
                "../libjpeg/jcarith.c",
		"../libjpeg/jccoefct.c",
                "../libjpeg/jccolor.c",
                "../libjpeg/jcdctmgr.c",
                "../libjpeg/jchuff.c",
                "../libjpeg/jcinit.c",
                "../libjpeg/jcmainct.c",
                "../libjpeg/jcmarker.c",
                "../libjpeg/jcmaster.c",
                "../libjpeg/jcomapi.c",
                "../libjpeg/jcparam.c",
                "../libjpeg/jcprepct.c",
                "../libjpeg/jcsample.c",
                "../libjpeg/jctrans.c",
                "../libjpeg/jdapimin.c",
                "../libjpeg/jdapistd.c",
		"../libjpeg/jdarith.c",
                "../libjpeg/jdatadst.c",
                "../libjpeg/jdatasrc.c",
                "../libjpeg/jdcoefct.c",
                "../libjpeg/jdcolor.c",
                "../libjpeg/jddctmgr.c",
                "../libjpeg/jdhuff.c",
                "../libjpeg/jdinput.c",
                "../libjpeg/jdmainct.c",
                "../libjpeg/jdmarker.c",
                "../libjpeg/jdmaster.c",
                "../libjpeg/jdmerge.c",
                "../libjpeg/jdpostct.c",
                "../libjpeg/jdsample.c",
                "../libjpeg/jdtrans.c",
                "../libjpeg/jerror.c",
                "../libjpeg/jfdctflt.c",
                "../libjpeg/jfdctfst.c",
                "../libjpeg/jfdctint.c",
                "../libjpeg/jidctflt.c",
                "../libjpeg/jidctfst.c",
                "../libjpeg/jidctint.c",
                "../libjpeg/jmemansi.c",
                # "../libjpeg/jmemdos.c",
                # "../libjpeg/jmemmac.c",
                "../libjpeg/jmemmgr.c",
                "../libjpeg/jmemname.c",
                "../libjpeg/jmemnobs.c",
                "../libjpeg/jpegtran.c",
                "../libjpeg/jquant1.c",
                "../libjpeg/jquant2.c",
                "../libjpeg/jutils.c",
                "../libjpeg/rdbmp.c",
                "../libjpeg/rdcolmap.c",
                "../libjpeg/rdgif.c",
                "../libjpeg/rdjpgcom.c",
                "../libjpeg/rdppm.c",
                "../libjpeg/rdrle.c",
                "../libjpeg/rdswitch.c",
                "../libjpeg/rdtarga.c",
                "../libjpeg/transupp.c",
                "../libjpeg/wrbmp.c",
                "../libjpeg/wrgif.c",
                "../libjpeg/wrjpgcom.c",
                "../libjpeg/wrppm.c",
                "../libjpeg/wrrle.c",
                "../libjpeg/wrtarga.c"
            ],
            "conditions": [
                [
                    "OS==\"linux\"",
                    {
                        "defines": [
                            "STDC_HEADERS"
                        ]
                    }
                ],
                [
                    "OS==\"mac\"",
                    {
                        "defines": [
                           # "USE_MAC_MEMMGR"
                        ],
                        "include_dirs": [
                            "platform-includes/mac/libjpeg"
                        ],
                        "sources" : [
                            # "../libjpeg/jmemmac.c"
                        ]
                    }
                ],
                [
                    "OS==\"win\"",
                    {
                        "defines": [
                            "USE_MSDOS_MEMMGR",
                            "MSDOS"
                        ],
                        "include_dirs": [
                            "platform-includes/win/libjpeg"
                        ],
                        "sources" : [
                            "../libjpeg/jmemdos.c"
                        ]
                    }
                ]
            ]
        }
    ]
}
