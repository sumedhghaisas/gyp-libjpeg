{    
    'targets': [
    {
      'target_name': 'jpeg_test',
      'dependencies': [
        '../bindings/libjpeg.gyp:libjpeg'
      ],
      'sources': [
        'cjpeg.c',
        "cjpeg_wrapper.cpp",
      ],
      "include_dirs": [
        "../libjpeg"
      ],
    }
  ]
}
