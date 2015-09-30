#include <iostream>
#include <string>

#include <node.h>
#include <v8.h>

using namespace std;
using namespace v8;

extern "C" int to_jpeg(const char* str_input_file, const char* str_output_file);

int to_jpeg_wrap(const string& str_input_file, const string& str_output_file)
{
  return to_jpeg(str_input_file.c_str(), str_output_file.c_str());
}

void com_to_jpeg(const FunctionCallbackInfo<v8::Value>& args)
{
  v8::Isolate* isolate;
  isolate = args.GetIsolate();
  if(args.Length() != 2)
  {
    args.GetReturnValue().Set(Undefined(isolate));
	return;
  }

  String::Utf8Value param1(args[0]->ToString());
  String::Utf8Value param2(args[1]->ToString());

  string input_filename(*param1);
  string output_filename(*param2);

  int status = to_jpeg_wrap(input_filename, output_filename);
  Local<Number> out = Number::New(isolate, status);
  args.GetReturnValue().Set(out);
  return;
}

void init(Handle<Object> exports) 
{
  Isolate* isolate = v8::Isolate::GetCurrent();
  exports->Set(String::NewFromUtf8(isolate, "toJpeg", v8::String::kInternalizedString),
      FunctionTemplate::New(isolate, com_to_jpeg)->GetFunction());
}
 
NODE_MODULE(jpeg_test, init)
  
  
